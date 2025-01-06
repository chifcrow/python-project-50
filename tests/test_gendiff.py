from hexlet_code.scripts.gendiff import generate_diff
import json


def test_generate_diff_json():
    file1 = 'tests/test_data/file1.json'
    file2 = 'tests/test_data/file2.json'
    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    actual_result = generate_diff(file1, file2)
    assert actual_result.strip() == expected_result.strip()


# Тест для file1.yml и file2.yml
def test_generate_diff_yaml():
    file1 = 'tests/test_data/file1.yml'
    file2 = 'tests/test_data/file2.yml'
    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    actual_result = generate_diff(file1, file2)
    assert actual_result.strip() == expected_result.strip()


# Тест для nested_file1.json и nested_file2.json

def test_generate_diff_nested():
    file1 = 'tests/test_data/nested_file1.json'
    file2 = 'tests/test_data/nested_file2.json'

    expected_result = """{
    common: {
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

    actual_result = generate_diff(file1, file2)

    # Удаляем лишние пробелы и сравниваем строки
    def normalize_output(output):
        return "\n".join([line.strip() for line in output.splitlines()])

    assert normalize_output(actual_result) == normalize_output(expected_result)


def test_generate_diff_plain():
    file1 = 'tests/test_data/nested_file1.json'
    file2 = 'tests/test_data/nested_file2.json'
    expected_result = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    actual_result = generate_diff(file1, file2, 'plain')
    assert actual_result.strip() == expected_result.strip()


def test_generate_diff_json_format():
    file1 = 'tests/test_data/nested_file1.json'
    file2 = 'tests/test_data/nested_file2.json'
    actual_result = generate_diff(file1, file2, format_name='json')

    # Пример ожидаемого результата
    expected_result = """
    {
        "common": {
            "key": "value",
            ...
        }
    }
    """  # Пример ожидаемого результата в формате JSON

    assert json.loads(actual_result) == json.loads(expected_result)
