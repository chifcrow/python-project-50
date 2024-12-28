import pytest
from hexlet_code.scripts.gendiff import generate_diff


@pytest.fixture
def file1():
    return "tests/test_data/file1.json"


@pytest.fixture
def file2():
    return "tests/test_data/file2.json"


@pytest.fixture
def expected_diff():
    with open("tests/test_data/expected_diff.txt") as f:
        return f.read()


def test_generate_diff(file1, file2, expected_diff):
    assert generate_diff(file1, file2) == expected_diff
