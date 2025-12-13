import json
import os

import pytest

from gendiff import generate_diff

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "test_data")


def get_fixture_path(filename: str) -> str:
    return os.path.join(FIXTURES_DIR, filename)


def read_fixture(filename: str) -> str:
    with open(get_fixture_path(filename), "r", encoding="utf-8") as f:
        return f.read()


@pytest.mark.parametrize(
    "file1,file2,expected_file",
    [
        ("file1.json", "file2.json", "expected_diff.txt"),
        ("file1.yml", "file2.yml", "expected_diff.txt"),
        ("nested_file1.json", "nested_file2.json", "expected_stylish.txt"),
    ],
)
def test_generate_diff_stylish(file1: str, file2: str,
                               expected_file: str) -> None:
    expected = read_fixture(expected_file).rstrip()
    result = generate_diff(get_fixture_path(file1),
                           get_fixture_path(file2)).rstrip()
    assert result == expected


def test_generate_diff_plain_nested() -> None:
    expected = read_fixture("expected_plain_nested.txt")
    result = generate_diff(
        get_fixture_path("nested_file1.json"),
        get_fixture_path("nested_file2.json"),
        format_name="plain",
    )
    assert result == expected


def test_generate_diff_json_nested() -> None:
    result = generate_diff(
        get_fixture_path("nested_file1.json"),
        get_fixture_path("nested_file2.json"),
        format_name="json",
    )
    parsed = json.loads(result)
    assert isinstance(parsed, list)
