"""Offline finite-task adapter. No provider, network, empirical runner or grading.

The future tested model may receive view() only, through separately authorized
transport. Python object privacy is not a sandbox; this repository contains keys.
"""
from copy import deepcopy
import hashlib
import json
import math

PUBLIC_FIELDS = {
    'task_id', 'purpose', 'candidates', 'initial_evidence', 'constraints',
    'decision_priorities', 'limits', 'rejection_policy', 'action_set',
}
TERMINAL_FIELDS = {
    'decision', 'selected_candidate_ids', 'implementation', 'source_ids',
    'constraints', 'unresolved', 'failure_reason', 'next_step', 'reason',
}
KINDS = {'INSPECT', 'COMPARE', 'REJECT', 'REOPEN', 'SELECT', 'HOLD', 'STOP'}
CONTRACT = {
    'request_fields': ['action_id', 'candidate_ids', 'response'],
    'request_types': 'action_id is a listed string; candidate_ids is a unique list of listed IDs; response is an object. No extra or duplicate JSON keys, nonfinite numbers, or JSON wrappers.',
    'nonterminal_response': {'reason': 'nonempty text, at most 40 whitespace-separated words; no other fields'},
    'terminal_response_fields': sorted(TERMINAL_FIELDS),
    'terminal_types': 'decision is SELECT, HOLD or STOP matching action_id; selected_candidate_ids equals candidate_ids; source_ids, constraints and unresolved are string lists; implementation, failure_reason, next_step and reason are strings. Cite only visible source IDs. All prose totals at most 300 whitespace-separated words, including reason (at most 40).',
    'candidate_arguments': 'INSPECT uses zero IDs, COMPARE two different IDs, REJECT/REOPEN one. SELECT may name listed candidates or describe an alternative instantiation or combination of supplied mechanisms supported by visible facts; implementation text is required and rejected candidates cannot be selected until reopened. HOLD/STOP use zero IDs. A new name or empty ID list is not automatic acceptance.',
    'reopening': 'REJECT retains all evidence and history. REOPEN requires reversible=true. COMPARE reveals no additional facts.',
    'charging': 'Every attempt counts toward max_attempts. INSPECT costs one unit, including duplicates and failed capture. Other valid actions cost zero. Malformed, unknown, unavailable or rejected attempts charge min(1,remaining units) and reveal no facts. Deadline_attempt applies to the attempted step, starting at 1.',
    'termination': 'No paid inspection may exceed acquisition_units. Exhausting units still permits a valid terminal action within max_attempts. Reaching max_attempts without a valid terminal decision ends as EFFORT_FAILURE. No actions follow a terminal decision. Intermediate rejection alone is not terminal failure.',
    'capture': 'Process state and observation are separate. A later capture failure cannot erase prior positive evidence. No released observation means no additional world fact.',
    'limits': 'Requests are limited to 16384 UTF-8 bytes. No external tool, source, permission or operating capability may be invented. These are toy acquisition units; model/token/time limits require a separate authorized transport.',
}
TEXT_FIELDS = {'implementation', 'failure_reason', 'next_step', 'reason'}
LIST_FIELDS = {'selected_candidate_ids', 'source_ids', 'constraints', 'unresolved'}


def _strings(value):
    return isinstance(value, list) and all(isinstance(x, str) for x in value)


def _unique_strings(value):
    return _strings(value) and len(value) == len(set(value))


def _integer(value, minimum=0):
    return type(value) is int and value >= minimum


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key')
        result[key] = value
    return result


def _constant(value):
    raise ValueError('nonfinite JSON number')


def _float(value):
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError('nonfinite JSON number')
    return parsed


def strict_json(raw):
    return json.loads(raw, object_pairs_hook=_pairs, parse_constant=_constant, parse_float=_float)


class Episode:
    def __init__(self, task, releases, *, surface=None):
        if set(task) != PUBLIC_FIELDS | {'surface1'}:
            raise ValueError('task shape does not match frozen public contract')
        for field in ('task_id', 'purpose'):
            if not isinstance(task[field], str) or not task[field].strip():
                raise ValueError('invalid task identity/purpose')
        shapes = {
            'candidates': {'id', 'summary', 'purpose', 'mechanism'},
            'constraints': {'id', 'text'},
            'decision_priorities': {'id', 'rank', 'text'},
        }
        for field, shape in shapes.items():
            rows = task[field]
            if not isinstance(rows, list) or not rows:
                raise ValueError('missing public records')
            identifiers = []
            for row in rows:
                if (not isinstance(row, dict) or set(row) != shape
                        or any(not isinstance(row[key], str) or not row[key].strip()
                               for key in shape - {'rank'})
                        or ('rank' in shape and not _integer(row['rank'], 1))):
                    raise ValueError('invalid nested public record')
                identifiers.append(row['id'])
            if len(identifiers) != len(set(identifiers)):
                raise ValueError('duplicate public record ID')
        self._task = deepcopy(task)
        self._surface = task['surface1'] if surface is None else surface
        if not isinstance(self._surface, str) or not self._surface.strip():
            raise ValueError('surface must be nonempty text')
        limits = task['limits']
        if (set(limits) != {'acquisition_units', 'max_attempts', 'invalid_attempt_cost_units'}
                or not _integer(limits['acquisition_units'])
                or not _integer(limits['max_attempts'], 1)
                or type(limits['invalid_attempt_cost_units']) is not int
                or limits['invalid_attempt_cost_units'] != 1):
            raise ValueError('invalid frozen limits')
        if (set(task['rejection_policy']) != {'reversible'}
                or type(task['rejection_policy']['reversible']) is not bool):
            raise ValueError('invalid rejection policy')
        self._candidate_ids = {row['id'] for row in task['candidates']}
        if (not self._candidate_ids or len(self._candidate_ids) != len(task['candidates'])
                or not all(isinstance(x, str) and x for x in self._candidate_ids)):
            raise ValueError('candidate IDs must be unique nonempty strings')
        evidence = task['initial_evidence']
        self._evidence = {}
        for row in evidence:
            self._validate_evidence(row)
            if row['id'] in self._evidence:
                raise ValueError('duplicate initial evidence')
            self._evidence[row['id']] = deepcopy(row)
        self._actions = {}
        release_ids = set()
        for row in task['action_set']:
            kind = row['kind']
            fields = {'action_id', 'kind', 'description', 'cost_units', 'deadline_attempt'}
            if kind == 'INSPECT':
                fields.add('target_evidence_id')
            if (kind not in KINDS or set(row) != fields
                    or type(row['cost_units']) is not int
                    or row['cost_units'] != (1 if kind == 'INSPECT' else 0)
                    or not _integer(row['deadline_attempt'], 1)
                    or row['deadline_attempt'] > limits['max_attempts']):
                raise ValueError('invalid frozen action')
            action_id = row['action_id']
            if (not isinstance(action_id, str) or action_id in self._actions
                    or action_id != ('INSPECT:' + row['target_evidence_id'] if kind == 'INSPECT' else kind)):
                raise ValueError('invalid action identity')
            self._actions[action_id] = deepcopy(row)
            if kind == 'INSPECT':
                identifier = row['target_evidence_id']
                if identifier in release_ids or identifier in self._evidence:
                    raise ValueError('evidence release ID collision')
                release_ids.add(identifier)
        if not (KINDS - {'INSPECT'}) <= set(self._actions):
            raise ValueError('missing common actions')
        if set(releases) != {x for x, a in self._actions.items() if a['kind'] == 'INSPECT'}:
            raise ValueError('release map does not match inspection catalogue')
        for action_id, release in releases.items():
            if (set(release) != {'process_state', 'evidence'}
                    or release['process_state'] not in {'CHECK_COMPLETED', 'FAILED_CAPTURE'}
                    or not isinstance(release['evidence'], list)
                    or len(release['evidence']) > 1):
                raise ValueError('invalid release shape')
            for row in release['evidence']:
                self._validate_evidence(row)
                if row['id'] != self._actions[action_id]['target_evidence_id']:
                    raise ValueError('release identity mismatch')
        self._releases = deepcopy(releases)
        self._inspected = set()
        self._rejected = set()
        self._history = []
        self._spent = 0
        self._terminal = None
        self._response = None

    @staticmethod
    def _validate_evidence(row):
        if (not isinstance(row, dict) or set(row) != {'id', 'text'}
                or not isinstance(row['id'], str) or not row['id']
                or not isinstance(row['text'], str) or not row['text']):
            raise ValueError('invalid evidence record')

    def view(self):
        result = {key: deepcopy(self._task[key]) for key in sorted(PUBLIC_FIELDS)
                  if key not in {'initial_evidence', 'action_set'}}
        result['surface'] = self._surface
        result['contract'] = deepcopy(CONTRACT)
        result['evidence'] = deepcopy(list(self._evidence.values()))
        result['action_set'] = []
        next_attempt = len(self._history) + 1
        for action in self._actions.values():
            row = deepcopy(action)
            row['available'] = (self._terminal is None
                and next_attempt <= action['deadline_attempt']
                and self._spent + action['cost_units'] <= self._task['limits']['acquisition_units'])
            result['action_set'].append(row)
        result['state'] = {
            'attempts': len(self._history),
            'attempts_remaining': self._task['limits']['max_attempts'] - len(self._history),
            'spent_units': self._spent,
            'units_remaining': self._task['limits']['acquisition_units'] - self._spent,
            'rejected_candidate_ids': sorted(self._rejected),
            'inspected_action_ids': sorted(self._inspected),
            'history': deepcopy(self._history),
            'terminal': self._terminal,
            'response': deepcopy(self._response),
        }
        return result

    def _request_error(self, request):
        if not isinstance(request, dict) or set(request) != {'action_id', 'candidate_ids', 'response'}:
            return 'REJECTED_REQUEST_SHAPE'
        if not isinstance(request['action_id'], str) or request['action_id'] not in self._actions:
            return 'REJECTED_UNKNOWN_ACTION'
        ids, response = request['candidate_ids'], request['response']
        if not _unique_strings(ids) or not set(ids) <= self._candidate_ids:
            return 'REJECTED_CANDIDATE_IDS'
        if not isinstance(response, dict) or not isinstance(response.get('reason'), str):
            return 'REJECTED_RESPONSE'
        if not response['reason'].strip() or len(response['reason'].split()) > 40:
            return 'REJECTED_REASON_LENGTH'
        action = self._actions[request['action_id']]
        kind = action['kind']
        if len(self._history) + 1 > action['deadline_attempt']:
            return 'REJECTED_DEADLINE'
        if kind in {'SELECT', 'HOLD', 'STOP'}:
            if (set(response) != TERMINAL_FIELDS or response['decision'] != kind
                    or any(not isinstance(response[x], str) for x in TEXT_FIELDS)
                    or any(not _strings(response[x]) for x in LIST_FIELDS)
                    or response['selected_candidate_ids'] != ids):
                return 'REJECTED_TERMINAL_SHAPE'
            if (not _unique_strings(response['source_ids'])
                    or not set(response['source_ids']) <= set(self._evidence)):
                return 'REJECTED_UNSEEN_CITATION'
            prose = [response[x] for x in TEXT_FIELDS] + response['constraints'] + response['unresolved']
            if sum(len(x.split()) for x in prose) > 300:
                return 'REJECTED_TERMINAL_LENGTH'
            if kind == 'SELECT':
                if set(ids) & self._rejected or not response['implementation'].strip():
                    return 'REJECTED_SELECTION'
            elif ids:
                return 'REJECTED_HOLD_STOP_SELECTION'
        else:
            if set(response) != {'reason'}:
                return 'REJECTED_NONTERMINAL_RESPONSE'
            expected = {'COMPARE': 2, 'REJECT': 1, 'REOPEN': 1, 'INSPECT': 0}[kind]
            if len(ids) != expected:
                return 'REJECTED_CANDIDATE_COUNT'
            if kind == 'REOPEN' and not self._task['rejection_policy']['reversible']:
                return 'REJECTED_IRREVERSIBLE'
        if self._spent + action['cost_units'] > self._task['limits']['acquisition_units']:
            return 'REJECTED_BUDGET'
        return None

    def submit(self, raw):
        if self._terminal is not None:
            raise ValueError('episode terminal; no further requests accepted')
        if not isinstance(raw, str):
            raise TypeError('transport must supply the original request text')
        record = {'attempt': len(self._history) + 1,
                  'request_sha256': hashlib.sha256(raw.encode()).hexdigest()}
        request = None
        try:
            if len(raw.encode()) > 16384:
                raise ValueError('request too large')
            request = strict_json(raw)
            error = self._request_error(request)
        except (ValueError, TypeError, KeyError, RecursionError):
            error = 'REJECTED_PARSE'
        # Preserve validly parsed requests; invalid bytes are bound by their digest.
        # Future authorized transport must retain raw wire records separately.
        if request is not None:
            record['request'] = deepcopy(request)
        record['status'] = error or 'APPLIED'
        requested_cost = 1 if error else self._actions[request['action_id']]['cost_units']
        remaining = self._task['limits']['acquisition_units'] - self._spent
        record['requested_units'] = requested_cost
        record['charged_units'] = min(requested_cost, remaining)
        self._spent += record['charged_units']
        if not error:
            action = self._actions[request['action_id']]
            kind, ids = action['kind'], request['candidate_ids']
            if kind == 'INSPECT':
                release = self._releases[request['action_id']]
                record['process_state'] = release['process_state']
                record['released_source_ids'] = [x['id'] for x in release['evidence']]
                if request['action_id'] in self._inspected:
                    record['status'] = 'DUPLICATE_INSPECTION'
                for row in release['evidence']:
                    self._evidence[row['id']] = deepcopy(row)
                self._inspected.add(request['action_id'])
            elif kind == 'REJECT':
                self._rejected.update(ids)
            elif kind == 'REOPEN':
                self._rejected.difference_update(ids)
            elif kind in {'SELECT', 'HOLD', 'STOP'}:
                self._terminal = kind
                self._response = deepcopy(request['response'])
        self._history.append(record)
        if len(self._history) == self._task['limits']['max_attempts'] and self._terminal is None:
            self._terminal = 'EFFORT_FAILURE'
        return self.view()
