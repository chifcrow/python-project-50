import json
import yaml


def parse(file_path):
    """
    Parses a file and returns its content as a dictionary.
    """
    _, extension = file_path.rsplit('.', 1)

    if extension in ('json',):
        with open(file_path) as file:
            return json.load(file)
    elif extension in ('yaml', 'yml'):
        with open(file_path) as file:
            return yaml.safe_load(file)
    else:
        raise ValueError(f"Unsupported file format: {extension}")
