from typing import Any, Callable, Dict, List

from .json_ import format_json
from .plain import format_plain
from .stylish import format_stylish


Formatter = Callable[[List[Dict[str, Any]]], str]


def format_diff(
    diff: List[Dict[str, Any]],
    format_name: str = "stylish",
) -> str:
    """Select formatter by name and format diff tree."""
    formatters: Dict[str, Formatter] = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json,
    }

    if format_name not in formatters:
        raise ValueError(f"Unsupported format: {format_name}")

    return formatters[format_name](diff)
