"""Freeze an offline instrument and planned assignment. Does not run any episode."""
import argparse
import hashlib
import json
from pathlib import Path
import random
import re

from adapter import Episode, strict_json

SEED = 20260907
STATUS = 'AUTHORED_INSTRUMENT_ONLY_NO_STUDY_NO_RESULTS'
FILES = (
    'README.md', 'TASKS.json', 'PRIVATE_KEYS.json', 'SURFACES.json', 'AUTHORING_NOTES.md',
    'SURFACE_REVIEW.md', 'adapter.py', 'test_adapter.py', 'prepare.py',
    '../MECHANISM_AND_COMPARATORS.md', '../PILOT_DECISION_SPEC.md',
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def instructions(directory):
    text = (directory / '../PILOT_DECISION_SPEC.md').read_text()
    blocks = re.findall(r'```text\n(.*?)\n```', text, flags=re.S)
    if len(blocks) != 4:
        raise ValueError('expected exactly Shared/O/M/R instruction strings')
    return {arm: '\n\n'.join(blocks[:count]) for arm, count in [('O', 2), ('M', 3), ('R', 4)]}


def materials(directory):
    tasks_bytes = (directory / 'TASKS.json').read_bytes()
    task_doc = strict_json(tasks_bytes)
    key_doc = strict_json((directory / 'PRIVATE_KEYS.json').read_text())
    surface_doc = strict_json((directory / 'SURFACES.json').read_text())
    tasks, keys, surfaces = task_doc['tasks'], key_doc['keys'], surface_doc['surfaces']
    if (len(tasks) != 12 or set(tasks) != set(keys) or set(tasks) != set(surfaces)
            or surface_doc['source_tasks_sha256'] != sha(tasks_bytes)):
        raise ValueError('task/key/surface parity or binding failed')
    if any(type(doc['schema_version']) is not int or doc['schema_version'] != 1
           for doc in (task_doc, key_doc, surface_doc)):
        raise ValueError('unknown material schema')
    for identifier, task in tasks.items():
        if task['task_id'] != identifier or set(surfaces[identifier]) != {'surface2'}:
            raise ValueError('task identity/surface shape failed')
        first = Episode(task, keys[identifier]['releases']).view()
        second = Episode(task, keys[identifier]['releases'], surface=surfaces[identifier]['surface2']).view()
        first.pop('surface'); second.pop('surface')
        if first != second:
            raise ValueError('surfaces changed shared information')
    cells = {(key['domain'], key['regime']) for key in keys.values()}
    if (len(cells) != 12 or len({x for x, _ in cells}) != 3
            or len({y for _, y in cells}) != 4):
        raise ValueError('authored 3-by-4 coverage incomplete')
    return tasks, keys, surfaces



def make_episode(directory, slot):
    """Instantiate one planned slot locally; caller may expose only its view."""
    tasks, keys, surfaces = materials(directory)
    task = dict(tasks[slot['task_id']])
    order = slot['candidate_order']
    candidates = {row['id']: row for row in task['candidates']}
    if len(order) != len(candidates) or set(order) != set(candidates):
        raise ValueError('planned candidate order is not a permutation')
    task['candidates'] = [candidates[identifier] for identifier in order]
    if slot['surface'] not in (1, 2) or type(slot['surface']) is not int:
        raise ValueError('unknown planned surface')
    surface = task['surface1'] if slot['surface'] == 1 else surfaces[task['task_id']]['surface2']
    return Episode(task, keys[task['task_id']]['releases'], surface=surface)


def public_prompt(directory, slot, episode):
    """Serialize instructions and public state only; no model or network call."""
    view = episode.view()
    if view['task_id'] != slot['task_id']:
        raise ValueError('episode does not match planned slot')
    return instructions(directory)[slot['arm']] + '\n\nPUBLIC_TASK_DATA\n' + json.dumps(view, ensure_ascii=False, allow_nan=False)


def build(directory):
    tasks, _, _ = materials(directory)
    arms = instructions(directory)
    blocks = [(task_id, surface, repeat) for task_id in sorted(tasks)
              for surface in (1, 2) for repeat in (1, 2)]
    rng = random.Random(SEED)
    rng.shuffle(blocks)
    slots = []
    for block, (identifier, surface, repeat) in enumerate(blocks, 1):
        arm_order = ['O', 'M', 'R']; rng.shuffle(arm_order)
        candidates = [x['id'] for x in tasks[identifier]['candidates']]
        rng.shuffle(candidates)
        for arm in arm_order:
            slots.append({'slot': len(slots) + 1, 'block': block, 'task_id': identifier,
                          'surface': surface, 'repeat': repeat, 'arm': arm,
                          'candidate_order': list(candidates), 'state': 'PLANNED_UNLAUNCHED'})
    return {
        'schema_version': 1, 'status': STATUS, 'assignment_seed': SEED,
        'planned_slots': len(slots), 'model_calls': 0, 'empirical_results': False,
        'purpose': 'Frozen local authoring record for execution review, not authorization or a run ledger.',
        'files': [{'path': name, 'bytes': len((directory/name).read_bytes()),
                   'sha256': sha((directory/name).read_bytes())} for name in FILES],
        'instruction_sha256': {arm: sha(text.encode()) for arm, text in arms.items()},
        'assignment': slots,
        'unresolved_execution': ['owner value and cost thresholds', 'exact model/provider/version and data handling',
                                 'authorized isolated transport with token/time/call enforcement and raw-wire retention',
                                 'reviewer allocation and final semantic acceptance', 'priced maximum and exact owner launch'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--confirm', choices=['AUTHORING_ONLY_NO_STUDY'])
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    expected = build(directory)
    output = directory / 'INSTRUMENT_MANIFEST.json'
    if args.write:
        if args.confirm != 'AUTHORING_ONLY_NO_STUDY':
            parser.error('--write requires --confirm AUTHORING_ONLY_NO_STUDY')
        output.write_text(json.dumps(expected, indent=2) + '\n')
        print('WROTE authored instrument manifest; 144 planned slots; zero model calls')
    else:
        if strict_json(output.read_text()) != expected:
            raise SystemExit('FAIL: instrument manifest differs from current authored sources')
        print('PASS: exact authored instrument, shared surface facts and 144 planned slots; zero model calls')


if __name__ == '__main__':
    main()
