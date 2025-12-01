from typing import Any, Dict, List


INDENT_SIZE = 4


def format_stylish(diff: List[Dict[str, Any]]) -> str:
    """Format diff tree in stylish format."""
    return _build_stylish(diff, depth=1)


def _build_stylish(nodes: List[Dict[str, Any]], depth: int) -> str:
    """Recursively build stylish representation for diff tree."""
    lines: List[str] = []
    indent = " " * (INDENT_SIZE * depth - 2)
    closing_indent = " " * (INDENT_SIZE * (depth - 1))

    lines.append("{")

    for node in nodes:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            children = node["children"]
            value = _build_stylish(children, depth + 1)
            lines.append(f"{indent}  {key}: {value}")
        elif node_type == "added":
            value = _stringify(node["value"], depth + 1)
            lines.append(f"{indent}+ {key}: {value}")
        elif node_type == "removed":
            value = _stringify(node["value"], depth + 1)
            lines.append(f"{indent}- {key}: {value}")
        elif node_type == "unchanged":
            value = _stringify(node["value"], depth + 1)
            lines.append(f"{indent}  {key}: {value}")
        elif node_type == "changed":
            old_value = _stringify(node["value1"], depth + 1)
            new_value = _stringify(node["value2"], depth + 1)
            lines.append(f"{indent}- {key}: {old_value}")
            lines.append(f"{indent}+ {key}: {new_value}")

    lines.append(f"{closing_indent}}}")
    return "\n".join(lines)


def _stringify(value: Any, depth: int) -> str:
    """Convert value to string with proper indentation for nested dicts."""
    if not isinstance(value, dict):
        return _to_str(value)

    lines: List[str] = []
    indent = " " * (INDENT_SIZE * depth)
    closing_indent = " " * (INDENT_SIZE * (depth - 1))

    lines.append("{")
    for key, val in value.items():
        nested_value = _stringify(val, depth + 1)
        lines.append(f"{indent}{key}: {nested_value}")
    lines.append(f"{closing_indent}}}")

    return "\n".join(lines)


def _to_str(value: Any) -> str:
    """Convert primitive values to string representation."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)
