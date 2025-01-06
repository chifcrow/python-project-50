def format_plain(diff, path=''):
    """
    Форматирует diff в формат plain.
    """
    lines = []
    for node in diff:
        key = node['key']
        property_path = f"{path}.{key}".lstrip('.')  # Формируем путь к свойству
        node_type = node['type']

        if node_type == 'nested':
            # Рекурсивно обрабатываем вложенные структуры
            lines.append(format_plain(node['children'], property_path))
        elif node_type == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{property_path}' was added with value: {value}")
        elif node_type == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif node_type == 'changed':
            value1 = format_value(node['value1'])
            value2 = format_value(node['value2'])
            lines.append(
                f"Property '{property_path}' was updated. From {value1} to {value2}")
        # Если значение не изменилось, ничего не добавляем для типа 'unchanged'

    return '\n'.join(lines)


def format_value(value):
    """
    Преобразует значение в строку, подходящую для plain.
    """
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    return value
