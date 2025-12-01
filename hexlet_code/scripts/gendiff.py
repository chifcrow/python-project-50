import argparse

from hexlet_code.gendiff import generate_diff as _generate_diff


def generate_diff(file1_path: str, file2_path: str,
                  format_name: str = "stylish") -> str:
    """Wrapper for library generate_diff to keep backward compatibility."""
    return _generate_diff(file1_path, file2_path, format_name)


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for gendiff."""
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", help="Path to the first file")
    parser.add_argument("second_file", help="Path to the second file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        default="stylish",
        dest="format",
    )
    return parser.parse_args()


def main() -> None:
    """CLI entry point."""
    args = parse_args()
    diff = _generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
