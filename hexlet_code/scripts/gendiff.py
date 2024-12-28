import argparse
import json


def read_file(file_path):
    """
    Reads and parses a JSON file.
    """
    with open(file_path) as file:
        return json.load(file)


def format_value(value):
    """
    Converts Python values to JSON-like string representation.
    """
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def build_diff(data1, data2):
    """
    Builds a diff between two dictionaries.
    """
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    return [build_diff_line(key, data1, data2) for key in all_keys]


def build_diff_line(key, data1, data2):
    """
    Builds a single diff line for the given key.
    """
    if key in data1 and key not in data2:
        return f"  - {key}: {format_value(data1[key])}"
    elif key not in data1 and key in data2:
        return f"  + {key}: {format_value(data2[key])}"
    elif data1[key] != data2[key]:
        return (
            f"  - {key}: {format_value(data1[key])}\n"
            f"  + {key}: {format_value(data2[key])}"
        )
    else:
        return f"    {key}: {format_value(data1[key])}"


def generate_diff(file1_path, file2_path, format_name='plain'):
    """
    Generates diff between two JSON files in a human-readable format.
    """
    data1 = read_file(file1_path)
    data2 = read_file(file2_path)
    diff_lines = build_diff(data1, data2)
    return "{\n" + "\n".join(diff_lines) + "\n}"


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='plain',
        dest='format'
    )
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
