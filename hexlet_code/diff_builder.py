def build_diff(data1, data2):
    """
    Builds a recursive diff tree between two data structures.
    """
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key not in data1:
            diff.append({'key': key, 'type': 'added', 'value': data2[key]})
        elif key not in data2:
            diff.append({'key': key, 'type': 'removed', 'value': data1[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key]),
            })
        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'type': 'changed',
                'value1': data1[key],
                'value2': data2[key],
            })
        else:
            diff.append({'key': key, 'type': 'unchanged', 'value': data1[key]})

    return diff
