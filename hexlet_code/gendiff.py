from hexlet_code.parsers import parse
from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters import format_diff


def generate_diff(
    file_path1: str,
    file_path2: str,
    format_name: str = "stylish",
) -> str:
    """Generate diff between two configuration files.

    :param file_path1: path to first file
    :param file_path2: path to second file
    :param format_name: output format: 'stylish', 'plain', or 'json'
    :return: formatted diff string
    """
    data1 = parse(file_path1)
    data2 = parse(file_path2)

    diff = build_diff(data1, data2)
    return format_diff(diff, format_name)
