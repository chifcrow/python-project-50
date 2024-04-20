# test_diff_generator.py

import json
from hexlet_code.scripts.diff_generator import generate_diff


def test_generate_diff_basic():
    data1 = {"key1": "value1", "key2": "value2"}
    data2 = {"key1": "value1", "key2": "new_value2"}

    expected_output = {
        "key1": "value1",
        "changes": {
            "- key2": "value2",
            "+ key2": "new_value2"
        }
    }
    assert json.loads(generate_diff(data1, data2)) == expected_output


def test_generate_diff_with_added_key():
    data1 = {"key1": "value1"}
    data2 = {"key1": "value1", "key2": "value2"}

    expected_output = {
        "key1": "value1",
        "changes": {
            "+ key2": "value2"
        }
    }
    assert json.loads(generate_diff(data1, data2)) == expected_output


def test_generate_diff_with_removed_key():
    data1 = {"key1": "value1", "key2": "value2"}
    data2 = {"key1": "value1"}

    expected_output = {
        "key1": "value1",
        "changes": {
            "- key2": "value2"
        }
    }
    assert json.loads(generate_diff(data1, data2)) == expected_output


def test_generate_diff_no_difference():
    data1 = {"key1": "value1"}
    data2 = {"key1": "value1"}

    expected_output = {
        "key1": "value1",
        "changes": {}
    }
    assert json.loads(generate_diff(data1, data2)) == expected_output
