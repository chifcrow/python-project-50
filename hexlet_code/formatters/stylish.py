def format_stylish(diff, depth=1):
    """
    Форматирует diff в стиль stylish.
    """
    indent_size = 4
    current_indent = ' ' * (depth * indent_size - 2)  # Отступ для текущего уровня
    closing_indent = ' ' * ((depth - 1) * indent_size)
    lines = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            children = format_stylish(node["children"], depth + 1)
            lines.append(f"{current_indent}  {key}: {children}")
        elif node_type == "unchanged":
            value = format_value(node["value"], depth)
            lines.append(f"{current_indent}  {key}: {value}")
        elif node_type == "removed":
            value = format_value(node["value"], depth)
            lines.append(f"{current_indent}- {key}: {value}")
        elif node_type == "added":
            value = format_value(node["value"], depth)
            lines.append(f"{current_indent}+ {key}: {value}")
        elif node_type == "changed":
            value1 = format_value(node["value1"], depth)
            value2 = format_value(node["value2"], depth)
            lines.append(f"{current_indent}- {key}: {value1}")
            lines.append(f"{current_indent}+ {key}: {value2}")

    result = "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"
    return result


def format_value(value, depth):
    """
    Форматирует значение для stylish.
    """
    indent_size = 4
    current_indent = ' ' * (depth * indent_size)
    closing_indent = ' ' * ((depth - 1) * indent_size)

    if isinstance(value, dict):
        formatted_lines = [
            f"{current_indent}{key}: {format_value(val, depth + 1)}"
            for key, val in value.items()
        ]
        return "{\n" + "\n".join(formatted_lines) + f"\n{closing_indent}}}"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)
