# python-project-50/hexlet_code/scripts/cli.py

import argparse
from hexlet_code.scripts.data_loader import load_data
from hexlet_code.scripts.diff_generator import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Generate differences between two files."
    )
    parser.add_argument('file1', help="First file")
    parser.add_argument('file2', help="Second file")
    args = parser.parse_args()

    data1 = load_data(args.file1)
    data2 = load_data(args.file2)

    print(generate_diff(data1, data2))


if __name__ == "__main__":
    main()
