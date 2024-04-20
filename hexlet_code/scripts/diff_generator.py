# python-project-50/hexlet_code/scripts/diff_generator.py

import json


def generate_diff(data1, data2):
    result = {"key1": data1.get("key1"), "changes": {}}
    all_keys = data1.keys() | data2.keys()

    for key in all_keys:
        if key in data1 and key not in data2:
            result["changes"]["- " + key] = data1[key]
        elif key in data2 and key not in data1:
            result["changes"]["+ " + key] = data2[key]
        elif data1[key] != data2[key]:
            result["changes"]["- " + key] = data1[key]
            result["changes"]["+ " + key] = data2[key]

    return json.dumps(result)
