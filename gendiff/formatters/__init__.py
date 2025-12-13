from typing import Any, Callable, Dict, List

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish

Formatter = Callable[[List[Dict[str, Any]]], str]

FORMATTERS: Dict[str, Formatter] = {
    "stylish": format_stylish,
    "plain": format_plain,
    "json": format_json,
}


def get_formatter(format_name: str) -> Formatter:
    formatter = FORMATTERS.get(format_name)
    if formatter is None:
        raise ValueError(f"Unknown format: {format_name}")
    return formatter
