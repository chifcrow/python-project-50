# python-project-50/hexlet_code/scripts/data_loader.py

import json


def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON.")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)
