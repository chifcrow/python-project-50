# python-project-50/hexlet_code/scripts/gendiff.py

import argparse
import json


def load_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def generate_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    lines = []

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

    return "{\n" + "\n".join(lines) + "\n}"


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument('first_file', help="first file to compare")
    parser.add_argument('second_file', help="second file to compare")
    parser.add_argument('-f', '--format', help="set format of output",
                        default='stylish')

    args = parser.parse_args()

    # Load JSON files
    data1 = load_json(args.first_file)
    data2 = load_json(args.second_file)

    # Generate and print the diff
    diff = generate_diff(data1, data2)
    print(diff)

    '''
    print(f"Comparing {args.first_file} and {args.second_file},"
          f" format: {args.format}")
    '''


if __name__ == "__main__":
    main()
