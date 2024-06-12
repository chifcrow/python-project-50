# python-project-50/hexlet_code/scripts/data_loader.py

import json
import logging

logging.basicConfig(level=logging.ERROR)


def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Error: File '{file_path}' does not exist.")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error: File '{file_path}' is not valid JSON.")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise
