# Gendiff — Difference Calculator

A CLI tool and Python library for comparing configuration files.
The project is implemented as part of the Hexlet course **“Difference Calculator”**.

---

## Project Status

[![Actions Status](https://github.com/chifcrow/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/chifcrow/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=chifcrow_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=chifcrow_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=chifcrow_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=chifcrow_python-project-50)

---

## Description

**Gendiff** is a command-line utility for calculating the difference between two configuration files.
It supports **JSON** and **YAML** formats and can output results in multiple representations.

The tool can be used as:

- a standalone CLI command
- an importable Python function

---

## Features

- Supports **JSON** and **YAML** files (`.json`, `.yml`, `.yaml`)
- Builds a structured difference tree:
  - `added`
  - `removed`
  - `changed`
  - `unchanged`
  - `nested`
- Provides three output formats:
  - **stylish** — human-readable tree view
  - **plain** — line-by-line change descriptions
  - **json** — structured JSON output for further processing

---

## Installation

### Using pip (recommended inside a virtual environment)

```bash
pip install -e .
```

After installation, the gendiff command becomes available.

### Using Makefile

```bash
make install
make build
make package-install
```

## Usage

### CLI

Show help:

```bash
gendiff -h
```

### Basic usage

```bash
gendiff <file_path1> <file_path2> --format <format>
```

- --format is optional
- default format is stylish
- available formats: stylish, plain, json

## Examples

```bash
gendiff file1.json file2.yml
gendiff --format plain file1.yml file2.yml
gendiff --format json file1.json file2.json
```

## Usage as a Library

```python
from gendiff import generate_diff

diff = generate_diff(
   "path/to/file1.yml",
   "path/to/file2.yml",
   format_name="plain",
)

print(diff)
```

## Output Example (stylish)

```text
{
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

## Project Structure

```text
gendiff/
├── __init__.py          # public API (generate_diff)
├── diff_builder.py      # builds diff tree
├── parsers.py           # JSON / YAML parsers
├── formatters/
│   ├── __init__.py      # formatter dispatcher
│   ├── stylish.py
│   ├── plain.py
│   └── json.py
└── scripts/
    └── gendiff.py       # CLI entry point
```

## Development

### Linting

```bash
make lint
```

### Auto-fix lint issues

```bash
make lint-fix
```

### Tests and Coverage

```bash
make test
```

Coverage reports are generated automatically and analyzed by SonarCloud in CI.

## Technologies

- Python 3.12
- PyYAML
- pytest / pytest-cov
- Ruff
- GitHub Actions (CI)
  SonarCloud (code quality & coverage)

## License

MIT License

Copyright (c) 2025 ChifCrow
