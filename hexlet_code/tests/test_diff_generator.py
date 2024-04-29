# test_diff_generator.py

import pytest  # type: ignore
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


def test_generate_diff_basic(data1, data2):
    result = generate_diff(data1, data2)
    expected_output = """{
    host: hexlet.io
  - follow: False
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    assert result.strip() == expected_output.strip()


def test_generate_diff_no_changes(data1):
    data_same_as_data1 = data1.copy()
    result = generate_diff(data1, data_same_as_data1)
    expected_output = """{
    host: hexlet.io
    timeout: 50
    proxy: 123.234.53.22
    follow: False
}"""
    assert result.strip() == expected_output.strip()


def test_generate_diff_all_changed(data1, data2):
    data2_modified = {
        "host": "hexlet.com",
        "timeout": 30,
        "proxy": "98.765.43.21",
        "verbose": False
    }
    result = generate_diff(data1, data2_modified)
    expected_output = """{
    host: hexlet.io
  - follow: False
  - proxy: 123.234.53.22
  + proxy: 98.765.43.21
  - timeout: 50
  + timeout: 30
  - verbose: True
  + verbose: False
}"""
    assert result.strip() == expected_output.strip()


def test_generate_diff_empty_data():
    result = generate_diff({}, {})
    expected_output = "{}"
    assert result.strip() == expected_output.strip()
