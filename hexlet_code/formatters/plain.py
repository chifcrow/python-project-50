from typing import Any, Dict, List


def format_plain(diff: List[Dict[str, Any]], parent: str = "") -> str:
    """Format diff tree into plain text representation."""
    lines: List[str] = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]

        property_path = f"{parent}.{key}" if parent else key

        if node_type == "nested":
            children = node["children"]
            nested_result = format_plain(children, property_path)
            if nested_result:
                lines.append(nested_result)
        elif node_type == "added":
            value = _stringify_plain(node["value"])
            lines.append(
                f"Property '{property_path}' was added with value: {value}",
            )
        elif node_type == "removed":
            lines.append(f"Property '{property_path}' was removed")
        elif node_type == "changed":
            old_value = _stringify_plain(node["value1"])
            new_value = _stringify_plain(node["value2"])
            lines.append(
                (
                    f"Property '{property_path}' was updated. "
                    f"From {old_value} to {new_value}"
                ),
            )
        # 'unchanged' is not included in plain format

    return "\n".join(lines)


def _stringify_plain(value: Any) -> str:
    """Convert value to string according to plain formatter rules."""
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)

    # strings should be wrapped in single quotes
    return f"'{value}'"
