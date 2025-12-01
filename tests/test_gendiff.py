import json
import os

from hexlet_code.gendiff import generate_diff


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "test_data")


def read_fixture(name: str) -> str:
    path = os.path.join(FIXTURES_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def test_generate_diff_json_stylish():
    file1 = os.path.join(FIXTURES_DIR, "file1.json")
    file2 = os.path.join(FIXTURES_DIR, "file2.json")

    expected = read_fixture("expected_diff.txt")
    actual = generate_diff(file1, file2, "stylish").strip()

    assert actual == expected


def test_generate_diff_yaml_stylish():
    file1 = os.path.join(FIXTURES_DIR, "file1.yml")
    file2 = os.path.join(FIXTURES_DIR, "file2.yml")

    expected = read_fixture("expected_diff.txt")
    actual = generate_diff(file1, file2, "stylish").strip()

    assert actual == expected


def test_generate_diff_nested_stylish():
    file1 = os.path.join(FIXTURES_DIR, "nested_file1.json")
    file2 = os.path.join(FIXTURES_DIR, "nested_file2.json")

    expected = read_fixture("expected_stylish.txt")
    actual = generate_diff(file1, file2, "stylish")

    # Normalize whitespace per line to avoid issues with indentation
    def normalize(output: str) -> str:
        return "\n".join(line.rstrip() for line in output.splitlines())

    assert normalize(actual) == normalize(expected)


def test_generate_diff_plain_flat():
    file1 = os.path.join(FIXTURES_DIR, "file1.json")
    file2 = os.path.join(FIXTURES_DIR, "file2.json")

    expected = read_fixture("expected_plain.txt")
    actual = generate_diff(file1, file2, "plain").strip()

    assert actual == expected


def test_generate_diff_plain_nested():
    file1 = os.path.join(FIXTURES_DIR, "nested_file1.json")
    file2 = os.path.join(FIXTURES_DIR, "nested_file2.json")

    expected = read_fixture("expected_plain_nested.txt")
    actual = generate_diff(file1, file2, "plain").strip()

    assert actual == expected


def test_generate_diff_json_format():
    file1 = os.path.join(FIXTURES_DIR, "file1.json")
    file2 = os.path.join(FIXTURES_DIR, "file2.json")

    output = generate_diff(file1, file2, "json")
    data = json.loads(output)

    # Basic structural checks; details проверяются форматером stylish/plain
    assert isinstance(data, list)
    assert all("key" in node and "type" in node for node in data)
