# python-project-50/hexlet_code/scripts/cli.py

import sys
import argparse
from hexlet_code.scripts.data_loader import load_json
from hexlet_code.scripts.diff_generator import generate_diff


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
    if len(sys.argv) < 3:
        print("Error: Two file paths are required")
        print("Usage: gendiff file1 file2")
        sys.exit(1)
    main()
