from typing import Any, Dict, List

Node = Dict[str, Any]
DiffTree = List[Node]


def build_diff(data1: Dict[str, Any], data2: Dict[str, Any]) -> DiffTree:
    keys = sorted(data1.keys() | data2.keys())
    diff: DiffTree = []

    for key in keys:
        if key not in data1:
            diff.append({"key": key, "type": "added", "value": data2[key]})
            continue

        if key not in data2:
            diff.append({"key": key, "type": "removed", "value": data1[key]})
            continue

        value1 = data1[key]
        value2 = data2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            children = build_diff(value1, value2)
            diff.append({"key": key, "type": "nested", "children": children})
            continue

        if value1 == value2:
            diff.append({"key": key, "type": "unchanged", "value": value1})
            continue

        diff.append(
            {
                "key": key,
                "type": "changed",
                "value1": value1,
                "value2": value2,
            }
        )

    return diff
