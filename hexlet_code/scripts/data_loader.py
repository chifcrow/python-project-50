# python-project-50/hexlet_code/scripts/data_loader.py

import json
import yaml
import logging

logging.basicConfig(level=logging.ERROR)


def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if file_path.endswith('.json'):
                return json.load(file)
            elif file_path.endswith(('.yml', '.yaml')):
                return yaml.safe_load(file)
            else:
                raise ValueError(f"Unsupported file format: {file_path}")
    except FileNotFoundError:
        logging.error(f"Error: File '{file_path}' does not exist.")
        raise
    except (json.JSONDecodeError, yaml.YAMLError):
        logging.error(f"Error: File '{file_path}' is not valid JSON or YAML.")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise
