# Gendiff — вычислитель отличий

CLI-утилита и библиотека для сравнения конфигурационных файлов.  
Проект выполнен в рамках курса Hexlet «Вычислитель отличий».

---

## Статус проекта

[![Actions Status](https://github.com/chifcrow/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/chifcrow/python-project-50/actions)
![CI](https://github.com/chifcrow/python-project-50/actions/workflows/ci.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/400671110001e36e8db4/maintainability)](https://codeclimate.com/github/chifcrow/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/400671110001e36e8db4/test_coverage)](https://codeclimate.com/github/chifcrow/python-project-50/test_coverage)

---

## Что умеет gendiff

- Сравнивает файлы форматов **JSON** и **YAML** (`.json`, `.yml`, `.yaml`)
- Строит дерево отличий (added / removed / changed / unchanged / nested)
- Поддерживает три формата вывода:
  - **stylish** — человекочитаемое древовидное отображение
  - **plain** — линейные описания изменений
  - **json** — структурированный JSON для дальнейшей обработки
- Работает как:
  - консольная команда `gendiff`
  - импортируемая функция `generate_diff()` из пакета `hexlet_code`

---

## Демонстрация (asciinema)

### 1. Сравнение плоских файлов (формат по умолчанию — `stylish`)

[![asciicast](https://asciinema.org/a/vQDipYFfH4xxDHwmS13AMmdgv.svg)](https://asciinema.org/a/vQDipYFfH4xxDHwmS13AMmdgv)

### 2. Сравнение вложенных структур (формат `stylish`)

[![asciicast](https://asciinema.org/a/j6I7sXEBXUtGjUKvcFvMwYaGr.svg)](https://asciinema.org/a/j6I7sXEBXUtGjUKvcFvMwYaGr)

### 3. Разные форматы вывода (`plain` и `json`)

[![asciicast](https://asciinema.org/a/YuhxQoSUUwE84fcEB5FVjFKKn.svg)](https://asciinema.org/a/YuhxQoSUUwE84fcEB5FVjFKKn)

## Установка

Рекомендуется использовать виртуальное окружение (`venv`).

```bash
git clone https://github.com/chifcrow/python-project-50.git
cd python-project-50

python -m venv venv
source venv/bin/activate   # Linux / macOS
# .\venv\Scripts\activate  # Windows PowerShell

pip install -e .
После установки команда gendiff становится доступна внутри venv.
```

### Использование (CLI)

Общий синтаксис:

```bash
gendiff [-f FORMAT] first_file second_file
```

Где:

first_file, second_file — пути к сравниваемым файлам

FORMAT — формат вывода: stylish (по умолчанию), plain, json

### Примеры

1. Формат по умолчанию (stylish)

```bash
gendiff tests/test_data/file1.json tests/test_data/file2.json
```

2. Формат plain

```bash
gendiff -f plain tests/test_data/file1.yml tests/test_data/file2.yml
```

3. Формат json

```bash
gendiff -f json tests/test_data/file1.json tests/test_data/file2.json
```

### Пример вывода (stylish)

```bash
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key: value
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
    }
  - group2: {
        abc: 12345
    }
  + group3: {
        deep: {
            id: 100500
        }
    }
}
```

### Использование как библиотеки

```bash
from hexlet_code import generate_diff

diff = generate_diff(
    "path/to/file1.yml",
    "path/to/file2.yml",
    format_name="plain",
)

print(diff)
```

### Структура проекта

```bash
hexlet_code/
  ├── __init__.py          # экспорт generate_diff
  ├── gendiff.py           # библиотечная функция generate_diff
  ├── parsers.py           # парсер JSON/YAML
  ├── diff_builder.py      # построение дерева diff
  ├── formatters/
  │     ├── __init__.py    # выбор форматера по имени
  │     ├── stylish.py     # формат stylish
  │     ├── plain.py       # формат plain
  │     └── json_.py       # формат json
  └── scripts/
        └── gendiff.py     # CLI entry point (argparse)
```

### Тесты и качество кода

- Локальный запуск линтера:

```bash
make lint
```

- Запуск тестов + генерация coverage.xml:

```bash
make test
```

Покрытие кода отправляется в Code Climate через GitHub Actions.

## Технологии

- Python 3.10
- PyYAML (поддержка YAML)
- pytest + pytest-cov
- flake8
- GitHub Actions (CI)
- Code Climate (coverage)

## Лицензия

Проект распространяется под лицензией MIT.

## Автор
