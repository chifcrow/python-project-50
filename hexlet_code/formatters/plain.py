def format_plain(diff, parent_path=""):
    """
    Форматирует diff в стиль plain.
    """
    lines = []
    for node in diff:
        key = node["key"]
        full_path = f"{parent_path}.{key}" if parent_path else key
        node_type = node["type"]

        if node_type == "nested":
            lines.append(format_plain(node["children"], full_path))
        elif node_type == "added":
            value = format_value_plain(node["value"])
            lines.append(f"Property '{full_path}' was added with value: {value}")
        elif node_type == "removed":
            lines.append(f"Property '{full_path}' was removed")
        elif node_type == "changed":
            old_value = format_value_plain(node["value1"])
            new_value = format_value_plain(node["value2"])
            lines.append(
                f"Property '{full_path}' was updated. From {old_value} to {new_value}")
    return "\n".join(lines)


def format_value_plain(value):
    """
    Форматирует значение для plain.
    """
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)
