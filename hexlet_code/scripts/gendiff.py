import argparse
import _json as json
from hexlet_code.parsers import parse


def read_file(file_path):
    """
    Reads and parses a JSON file.
    """
    with open(file_path) as file:
        return json.load(file)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    return [build_diff_line(key, data1, data2) for key in all_keys]


def build_diff_line(key, data1, data2):
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
    data1 = parse(file1_path)
    data2 = parse(file2_path)
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
