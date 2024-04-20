# python-project-50/hexlet_code/scripts/cli.py

import argparse
from data_loader import load_json
from diff_generator import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Generate differences between two JSON files."
    )
    parser.add_argument('file1', help="First JSON file")
    parser.add_argument('file2', help="Second JSON file")
    args = parser.parse_args()

    data1 = load_json(args.file1)
    data2 = load_json(args.file2)

    print(generate_diff(data1, data2))


if __name__ == "__main__":
    main()
