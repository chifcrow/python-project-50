import argparse
import sys

from gendiff.gendiff import generate_diff


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        help="set format of output",
        dest="format_name",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        result = generate_diff(args.first_file,
                               args.second_file, args.format_name)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2) from exc

    print(result)


if __name__ == "__main__":
    main()
