import argparse
from hexlet_code.parsers import parse
from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters.stylish import format_stylish


def generate_diff(file1_path, file2_path, format_name='stylish'):
    """
    Generates a diff between two files in the specified format.
    """
    data1 = parse(file1_path)
    data2 = parse(file2_path)
    diff = build_diff(data1, data2)
    if format_name == 'stylish':
        return format_stylish(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish',
        dest='format'
    )
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
