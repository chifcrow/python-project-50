import json


def format_json(diff):
    """
    Форматирует diff в JSON формат.
    """
    return json.dumps(diff, indent=4)
