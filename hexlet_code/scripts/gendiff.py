import argparse


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument('first_file', help="first file to compare")
    parser.add_argument('second_file', help="second file to compare")
    parser.add_argument('-f', '--format', help="set format of output",
                        default='stylish')

    args = parser.parse_args()
    print(f"Comparing {args.first_file} and {args.second_file},"
          f" format: {args.format}")


if __name__ == "__main__":
    main()
