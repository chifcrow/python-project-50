from typing import Any, Dict, List


def format_plain(diff: List[Dict[str, Any]]) -> str:
    lines = _iter_plain(diff)
    result = "\n".join(lines)
    return f"{result}\n" if result else ""


def _iter_plain(diff: List[Dict[str, Any]], parent: str = "") -> List[str]:
    lines: List[str] = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]
        full_key = f"{parent}.{key}" if parent else key

        if node_type == "nested":
            children = node.get("children", [])
            lines.extend(_iter_plain(children, full_key))

        elif node_type == "added":
            value = _stringify_value(node["value"])
            lines.append(
                f"Property '{full_key}' was added with value: {value}")

        elif node_type == "removed":
            lines.append(f"Property '{full_key}' was removed")

        elif node_type == "changed":
            value1 = _stringify_value(node["value1"])
            value2 = _stringify_value(node["value2"])
            lines.append(
                f"Property '{full_key}' was updated. From {value1} to {value2}"
            )

        elif node_type == "unchanged":
            continue

        else:
            raise ValueError(f"Unknown node type: {node_type}")

    return lines


def _stringify_value(value: Any) -> str:
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, list):
        return "[complex value]"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
