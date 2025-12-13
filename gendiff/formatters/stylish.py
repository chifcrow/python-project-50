from typing import Any, Dict, List

INDENT_SIZE = 4
SHIFT = 2


def format_stylish(diff: List[Dict[str, Any]]) -> str:
    body = _iter_stylish(diff, depth=1)
    return "{\n" + body + "\n}"


def _iter_stylish(diff: List[Dict[str, Any]], depth: int) -> str:
    lines: List[str] = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            children = node.get("children", [])
            inner = _iter_stylish(children, depth + 1)
            value = "{\n" + inner + "\n" + _indent(depth) + "}"
            lines.append(_format_line(" ", key, value, depth))

        elif node_type == "added":
            value = _stringify(node["value"], depth + 1)
            lines.append(_format_line("+", key, value, depth))

        elif node_type == "removed":
            value = _stringify(node["value"], depth + 1)
            lines.append(_format_line("-", key, value, depth))

        elif node_type == "unchanged":
            value = _stringify(node["value"], depth + 1)
            lines.append(_format_line(" ", key, value, depth))

        elif node_type == "changed":
            value1 = _stringify(node["value1"], depth + 1)
            value2 = _stringify(node["value2"], depth + 1)
            lines.append(_format_line("-", key, value1, depth))
            lines.append(_format_line("+", key, value2, depth))

        else:
            raise ValueError(f"Unknown node type: {node_type}")

    return "\n".join(lines)


def _format_line(prefix: str, key: str, value: str, depth: int) -> str:
    indent = _indent(depth, with_shift=True)
    # Hexlet expects "key: " (with trailing space) for empty string values
    if value == "":
        return f"{indent}{prefix} {key}: "
    return f"{indent}{prefix} {key}: {value}"


def _stringify(value: Any, depth: int) -> str:
    if isinstance(value, dict):
        return _stringify_dict(value, depth)
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if value == "":
        return ""
    return str(value)


def _stringify_dict(value: Dict[str, Any], depth: int) -> str:
    lines: List[str] = []

    for k, v in value.items():
        rendered = _stringify(v, depth + 1)
        # Same rule inside nested dicts: "key: " for empty strings
        if rendered == "":
            lines.append(f"{_indent(depth)}{k}: ")
        else:
            lines.append(f"{_indent(depth)}{k}: {rendered}")

    return "{\n" + "\n".join(lines) + "\n" + _indent(depth - 1) + "}"


def _indent(depth: int, with_shift: bool = False) -> str:
    size = depth * INDENT_SIZE - (SHIFT if with_shift else 0)
    return " " * size
