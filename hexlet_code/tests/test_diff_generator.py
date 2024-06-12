# test_diff_generator.py

import pytest
import json
import yaml
from hexlet_code.scripts.diff_generator import generate_diff


@pytest.fixture
def data1():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }


@pytest.fixture
def data2():
    return {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }


@pytest.fixture
def data2_modified():
    return {
        "host": "hexlet.com",
        "timeout": 30,
        "proxy": "98.765.43.21",
        "verbose": False
    }


def convert_to_json(data):
    return json.dumps(data)


def convert_to_yaml(data):
    return yaml.dump(data)


@pytest.mark.parametrize("convert", [convert_to_json, convert_to_yaml])
def test_generate_diff_basic(data1, data2, convert):
    data1_str = convert(data1)
    data2_str = convert(data2)
    data1_loaded = (
        json.loads(data1_str)
        if convert == convert_to_json
        else yaml.safe_load(data1_str)
    )
    data2_loaded = (
        json.loads(data2_str)
        if convert == convert_to_json
        else yaml.safe_load(data2_str)
    )

    result = generate_diff(data1_loaded, data2_loaded)
    expected_output = """
{
  - follow: False
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
  host: hexlet.io
}""".strip()
    assert result == expected_output


@pytest.mark.parametrize("convert", [convert_to_json, convert_to_yaml])
def test_generate_diff_no_changes(data1, convert):
    data1_str = convert(data1)
    data1_loaded = (
        json.loads(data1_str)
        if convert == convert_to_json
        else yaml.safe_load(data1_str)
    )
    result = generate_diff(data1_loaded, data1_loaded)
    expected_output = """
{
  follow: False
  host: hexlet.io
  proxy: 123.234.53.22
  timeout: 50
}""".strip()
    assert result == expected_output


@pytest.mark.parametrize("convert", [convert_to_json, convert_to_yaml])
def test_generate_diff_all_changed(data1, data2_modified, convert):
    data1_str = convert(data1)
    data2_modified_str = convert(data2_modified)
    data1_loaded = (
        json.loads(data1_str)
        if convert == convert_to_json
        else yaml.safe_load(data1_str)
    )
    data2_modified_loaded = (
        json.loads(data2_modified_str)
        if convert == convert_to_json
        else yaml.safe_load(data2_modified_str)
    )

    result = generate_diff(data1_loaded, data2_modified_loaded)
    expected_output = """
{
  - follow: False
  - proxy: 123.234.53.22
  + proxy: 98.765.43.21
  - timeout: 50
  + timeout: 30
  - verbose: True
  + verbose: False
  host: hexlet.io
  + host: hexlet.com
}""".strip()
    assert result == expected_output


@pytest.mark.parametrize("convert", [convert_to_json, convert_to_yaml])
def test_generate_diff_empty_data(convert):
    result = generate_diff({}, {})
    expected_output = "{}"
    assert result == expected_output
