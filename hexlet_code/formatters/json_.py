import json
from typing import Any, Dict, List


def format_json(diff: List[Dict[str, Any]]) -> str:
    """Format diff tree as JSON string."""
    return json.dumps(diff, indent=2)
