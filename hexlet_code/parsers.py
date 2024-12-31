import os
import json
import yaml


def parse(file_path):
    """
    Parses a file and returns its content as a dictionary.
    Supports JSON and YAML formats.
    """
    # Если путь не абсолютный, ищем файл в текущей директории
    if not os.path.isabs(file_path):
        if os.path.exists(file_path):
            full_path = file_path
        else:
            # Если файл не найден, проверяем стандартные папки
            test_data_path = os.path.join('tests', 'test_data', file_path)
            if os.path.exists(test_data_path):
                full_path = test_data_path
            else:
                raise FileNotFoundError(f"File '{file_path}' not found.")
    else:
        full_path = file_path

    # Определяем расширение файла
    _, extension = os.path.splitext(full_path)

    # Парсим содержимое файла
    if extension in ('.json',):
        with open(full_path) as file:
            return json.load(file)
    elif extension in ('.yaml', '.yml'):
        with open(full_path) as file:
            return yaml.safe_load(file)
    else:
        raise ValueError(f"Unsupported file format: {extension}")
