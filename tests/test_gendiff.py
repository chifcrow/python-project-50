from hexlet_code.scripts.gendiff import generate_diff


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
