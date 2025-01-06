# gendiff

CLI-утилита для сравнения конфигурационных файлов.

## Hexlet tests and linter status

[![Actions Status](https://github.com/chifcrow/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/chifcrow/python-project-50/actions)

![CI](https://github.com/chifcrow/python-project-50/actions/workflows/ci.yml/badge.svg)

## Maintainability status

[![Maintainability](https://api.codeclimate.com/v1/badges/400671110001e36e8db4/maintainability)](https://codeclimate.com/github/chifcrow/python-project-50/maintainability)

## Code Climate status

[![Test Coverage](https://api.codeclimate.com/v1/badges/400671110001e36e8db4/test_coverage)](https://codeclimate.com/github/chifcrow/python-project-50/test_coverage)

## Поддерживаемые форматы

- JSON
- YAML

## Установка

Убедитесь, что у вас установлен Python версии 3.10 или выше. Затем выполните следующие шаги:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/chifcrow/python-project-50.git
   cd python-project-50
   ```

2. Установите зависимости:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Использование

Пример использования для сравнения файлов в формате JSON и YAML:

gendiff file1.json file2.yml
Пример использования с выводом в формате plain:

```bash
gendiff --format plain file1.json file2.json
```

## Тестирование и проверка проекта

1. Запуск тестов
   Выполните команду для запуска всех тестов:

```bash
pytest -vv
```

2. Линтинг кода
   Для проверки кода на соответствие стандартам выполните:

```bash
make lint
```

3. Запуск примера
   Для проверки работы утилиты выполните:

```bash
python -m hexlet_code.scripts.gendiff --format plain tests/test_data/nested_file1.json tests/test_data/nested_file2.json
```

## Форматы вывода

Формат по умолчанию (stylish)

Пример результата:

```plaintext
{
common: {
setting1: Value 1 - setting2: 200 - setting3: true + setting3: null + setting4: blah blah
setting6: {
doge: { - wow: + wow: so much
}
key: value + ops: vops
}
}
group1: { - baz: bas + baz: bars
foo: bar - nest: {
key: value
} + nest: str
}

- group2: {
  abc: 12345
  deep: {
  id: 45
  }
  }

* group3: {
  deep: {
  id: {
  number: 45
  }
  }
  fee: 100500
  }
  }
```

## Формат plain

Пример результата:

```plaintext
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```

## Лицензия

Этот проект распространяется под лицензией MIT.
