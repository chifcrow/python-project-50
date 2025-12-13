from gendiff.diff_builder import build_diff
from gendiff.formatters import get_formatter
from gendiff.parser import parse


def generate_diff(file1_path: str, file2_path: str,
                  format_name: str = "stylish") -> str:
    data1 = parse(file1_path)
    data2 = parse(file2_path)
    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff)
