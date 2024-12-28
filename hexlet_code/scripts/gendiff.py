import argparse
import json


def format_value(value):
    """
    Приводит значения Python к строковому виду, соответствующему JSON.
    """
    if isinstance(value, bool):
        return str(value).lower()  # True -> true, False -> false
    if value is None:
        return 'null'
    return value


def generate_diff(file1_path, file2_path, format_name='plain'):
    """
    Generates diff between two JSON files in a human-readable format.
    """
    # Читаем данные из файлов
    data1 = json.load(open(file1_path))
    data2 = json.load(open(file2_path))

    # Собираем ключи из обоих словарей, чтобы они были уникальными и отсортированными
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    # Формируем список изменений
    diff_lines = []

    for key in all_keys:
        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1 and key in data2:
            diff_lines.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] != data2[key]:
            diff_lines.append(f"  - {key}: {format_value(data1[key])}")
            diff_lines.append(f"  + {key}: {format_value(data2[key])}")
        else:
            diff_lines.append(f"    {key}: {format_value(data1[key])}")

    # Возвращаем результат в виде строки
    return "{\n" + "\n".join(diff_lines) + "\n}"


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='plain',
        dest='format'
    )
    args = parser.parse_args()

    # Генерируем diff и выводим результат
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
