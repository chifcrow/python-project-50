import json
import os
from typing import Any

import yaml


def parse(file_path: str) -> Any:
    """Read file and parse its content to Python data structure.

    Supports JSON (.json) and YAML (.yml, .yaml).
    """
    _, ext = os.path.splitext(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if ext == ".json":
        return json.loads(content)
    if ext in (".yml", ".yaml"):
        return yaml.safe_load(content)

    raise ValueError(f"Unsupported file format: '{ext}'")
