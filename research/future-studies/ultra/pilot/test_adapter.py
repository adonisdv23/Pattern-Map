"""Adversarial offline contract checks; these are not model episodes or results."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from adapter import Episode, strict_json


def specimen():
    kinds = ['COMPARE', 'REJECT', 'REOPEN', 'SELECT', 'HOLD', 'STOP']
    task = {
        'task_id': 'SAMPLE', 'purpose': 'Inspect a fictional local condition.',
        'surface1': 'A fixture for adapter behavior, excluded from pilot tasks.',
        'candidates': [{'id': 'C1', 'summary': 'One route', 'purpose': 'Function', 'mechanism': 'Method'},
                       {'id': 'C2', 'summary': 'Another route', 'purpose': 'Function', 'mechanism': 'Other'}],
        'initial_evidence': [{'id': 'E1', 'text': 'Initial observation'}],
        'constraints': [{'id': 'Q1', 'text': 'Preserve the boundary'}],
        'decision_priorities': [{'id': 'P1', 'rank': 1, 'text': 'Meet Q1'}],
        'limits': {'acquisition_units': 2, 'max_attempts': 6, 'invalid_attempt_cost_units': 1},
        'rejection_policy': {'reversible': True},
        'action_set': [dict(action_id=k, kind=k, description=k, cost_units=0, deadline_attempt=6) for k in kinds]
            + [dict(action_id='INSPECT:E2', kind='INSPECT', description='Inspect condition', cost_units=1,
                    deadline_attempt=3, target_evidence_id='E2')],
    }
    releases = {'INSPECT:E2': {'process_state': 'FAILED_CAPTURE',
                              'evidence': [{'id': 'E2', 'text': 'A positive event was found before later capture failure.'}]}}
    return task, releases


def request(action, ids=None, **changes):
    ids = [] if ids is None else ids
    response = {'reason': 'A brief declared reason.'}
    if action in {'SELECT', 'HOLD', 'STOP'}:
        response.update(decision=action, selected_candidate_ids=ids,
                        implementation='Candidate method' if action == 'SELECT' else '',
                        source_ids=['E1'], constraints=['Q1'], unresolved=[],
                        failure_reason='A missing condition would defeat it.', next_step='No external action.')
    response.update(changes)
    return json.dumps({'action_id': action, 'candidate_ids': ids, 'response': response})


class AdapterContract(unittest.TestCase):
    def episode(self, **limits):
        task, releases = specimen()
        task['limits'].update(limits)
        for action in task['action_set']:
            action['deadline_attempt'] = min(action['deadline_attempt'], task['limits']['max_attempts'])
        return Episode(task, releases)

    def test_allowlisted_view_no_private_releases_and_copy_isolation(self):
        episode = self.episode()
        initial = episode.view()
        self.assertNotIn('positive event', json.dumps(initial))
        self.assertNotIn('process_state', json.dumps(initial))
        self.assertEqual(initial['contract']['request_fields'], ['action_id', 'candidate_ids', 'response'])
        self.assertIn('selected_candidate_ids', initial['contract']['terminal_response_fields'])
        initial['candidates'][0]['summary'] = 'mutated copy'
        self.assertNotEqual(initial['candidates'], episode.view()['candidates'])
        self.assertEqual(strict_json(json.dumps(episode.view(), allow_nan=False)), episode.view())
        task, releases = specimen()
        task['private_key'] = 'HIDDEN'
        with self.assertRaisesRegex(ValueError, 'shape'):
            Episode(task, releases)
        for field in ('candidates', 'constraints', 'decision_priorities'):
            task, releases = specimen()
            task[field][0]['private_answer'] = 'HIDDEN'
            with self.assertRaisesRegex(ValueError, 'nested'):
                Episode(task, releases)

    def test_action_description_is_text_and_irreversibility_is_visible(self):
        task, releases = specimen()
        task['action_set'][0]['description'] = {'private_answer': 'SYNTHETIC_CANARY'}
        with self.assertRaisesRegex(ValueError, 'action'):
            Episode(task, releases)
        task, releases = specimen()
        task['rejection_policy']['reversible'] = False
        episode = Episode(task, releases)
        view = episode.submit(request('REJECT', ['C1']))
        reopen = next(x for x in view['action_set'] if x['kind'] == 'REOPEN')
        self.assertFalse(reopen['available'])
        rejected = episode.submit(request('REOPEN', ['C1']))
        self.assertEqual(rejected['state']['history'][-1]['status'], 'REJECTED_IRREVERSIBLE')

    def test_duplicate_failure_costs_and_presence_survives_failed_capture(self):
        episode = self.episode()
        first = episode.submit(request('INSPECT:E2'))
        second = episode.submit(request('INSPECT:E2'))
        self.assertEqual(first['state']['history'][0]['process_state'], 'FAILED_CAPTURE')
        self.assertEqual(second['state']['spent_units'], 2)
        self.assertEqual(second['state']['history'][1]['status'], 'DUPLICATE_INSPECTION')
        self.assertEqual([x['id'] for x in second['evidence']], ['E1', 'E2'])
        self.assertEqual(second['state']['terminal'], None)

    def test_budget_failure_still_allows_terminal_within_attempt_limit(self):
        episode = self.episode(acquisition_units=0)
        failed = episode.submit(request('INSPECT:E2'))
        self.assertEqual(failed['state']['history'][-1]['status'], 'REJECTED_BUDGET')
        self.assertEqual(failed['state']['history'][-1]['charged_units'], 0)
        self.assertEqual(len(failed['evidence']), 1)
        selected = episode.submit(request('SELECT', ['C1']))
        self.assertEqual(selected['state']['terminal'], 'SELECT')
        before = episode.view()
        with self.assertRaisesRegex(ValueError, 'terminal'):
            episode.submit(request('STOP'))
        self.assertEqual(before, episode.view())

    def test_all_attempts_count_and_last_terminal_is_valid(self):
        episode = self.episode(max_attempts=2)
        episode.submit(request('COMPARE', ['C1', 'C2']))
        ending = episode.submit(request('REJECT', ['C1']))
        self.assertEqual(ending['state']['terminal'], 'EFFORT_FAILURE')
        episode = self.episode(max_attempts=2)
        episode.submit('not JSON')
        self.assertEqual(episode.submit(request('HOLD'))['state']['terminal'], 'HOLD')

    def test_malformed_duplicate_nonfinite_and_wrong_shapes_are_retained(self):
        invalid = ['{', '{}', '[]', 'null', '{"a":1,"a":2}',
                   '{"x":NaN}', '{"x":Infinity}', '{"x":1e999}',
                   request('NO_SUCH_ACTION'), request('COMPARE', ['C1', 'C1']),
                   request('INSPECT:E2', ['C1']), request('SELECT', ['C1'], extra='forbidden'),
                   request('SELECT', ['C1'], source_ids=['E2']),
                   request('HOLD', ['C1']), request('STOP', reason='x ' * 41),
                   request('SELECT', ['C1'], implementation='x ' * 301)]
        for raw in invalid:
            with self.subTest(raw=raw[:60]):
                result = self.episode().submit(raw)
                event = result['state']['history'][0]
                self.assertTrue(event['status'].startswith('REJECTED'))
                self.assertEqual(event['charged_units'], 1)
                self.assertEqual(result['state']['attempts'], 1)
                self.assertEqual(len(event['request_sha256']), 64)
                self.assertEqual(len(result['evidence']), 1)
                json.dumps(result, allow_nan=False)

    def test_deadlines_and_reopening_keep_history_and_evidence(self):
        episode = self.episode()
        episode.submit(request('REJECT', ['C1']))
        episode.submit(request('INSPECT:E2'))
        rejected = episode.submit(request('SELECT', ['C1']))
        self.assertEqual(rejected['state']['history'][-1]['status'], 'REJECTED_SELECTION')
        episode.submit(request('REOPEN', ['C1']))
        deadline = episode.submit(request('INSPECT:E2'))
        self.assertEqual(deadline['state']['history'][-1]['status'], 'REJECTED_DEADLINE')
        final = episode.submit(request('SELECT', ['C1'], source_ids=['E1', 'E2']))
        self.assertEqual(final['state']['terminal'], 'SELECT')
        self.assertEqual(len(final['state']['history']), 6)
        self.assertEqual([x['id'] for x in final['evidence']], ['E1', 'E2'])

    def test_zero_evidence_failure_and_bad_release_identity(self):
        task, releases = specimen()
        releases['INSPECT:E2']['evidence'] = []
        result = Episode(task, releases).submit(request('INSPECT:E2'))
        self.assertEqual(result['state']['history'][-1]['process_state'], 'FAILED_CAPTURE')
        self.assertEqual(len(result['evidence']), 1)
        task, releases = specimen()
        releases['INSPECT:E2']['evidence'][0]['id'] = 'UNRELATED'
        with self.assertRaisesRegex(ValueError, 'identity'):
            Episode(task, releases)

    def test_unforeseen_implementation_goes_to_semantic_review(self):
        result = self.episode().submit(request('SELECT', ['C1'], implementation='An unforeseen implementation of the supplied mechanism'))
        self.assertEqual(result['state']['terminal'], 'SELECT')
        self.assertNotIn('accepted', result)
        self.assertNotIn('score', result)
        empty = self.episode().submit(request('SELECT', [], implementation='Renamed rejected route'))
        self.assertEqual(empty['state']['history'][-1]['status'], 'REJECTED_SELECTION')

    def test_loaded_packets_match_strict_contract(self):
        directory = Path(__file__).parent
        if not (directory / 'TASKS.json').exists():
            self.fail('required frozen task material is missing')
        tasks = strict_json((directory / 'TASKS.json').read_text())['tasks']
        keys = strict_json((directory / 'PRIVATE_KEYS.json').read_text())['keys']
        self.assertEqual(len(tasks), 12)
        self.assertEqual(set(tasks), set(keys))
        for identifier, task in tasks.items():
            with self.subTest(task=identifier):
                episode = Episode(task, keys[identifier]['releases'])
                first = episode.view()
                self.assertEqual(first['task_id'], identifier)
                self.assertFalse({'rubric', 'regime', 'domain', 'releases'} & set(first))
                for action in task['action_set']:
                    if action['kind'] == 'INSPECT':
                        solo = Episode(task, keys[identifier]['releases'])
                        output = solo.submit(request(action['action_id']))
                        self.assertEqual(output['state']['history'][0]['status'], 'APPLIED')
                        for row in keys[identifier]['releases'][action['action_id']]['evidence']:
                            self.assertIn(row, output['evidence'])


if __name__ == '__main__':
    unittest.main()
