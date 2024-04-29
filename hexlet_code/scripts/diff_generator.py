# python-project-50/hexlet_code/scripts/diff_generator.py


def generate_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    lines = ["{"]

    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)
        if key in data1 and key not in data2:
            lines.append(f"  - {key}: {val1}")
        elif key in data2 and key not in data1:
            lines.append(f"  + {key}: {val2}")
        elif val1 != val2:
            lines.append(f"  - {key}: {val1}")
            lines.append(f"  + {key}: {val2}")
        else:
            lines.append(f"    {key}: {val1}")

    lines.append("}")
    return "\n".join(lines)
