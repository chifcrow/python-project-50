# Gendiff — Difference Calculator

A CLI tool and Python library for comparing configuration files.  
Implemented as part of the Hexlet “Difference Calculator” project.

---

## Status

[![Actions Status](https://github.com/chifcrow/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/chifcrow/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=chifcrow_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=chifcrow_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=chifcrow_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=chifcrow_python-project-50)

---

## Description

**Gendiff** calculates the difference between two configuration files and prints it in one of the supported formats.

Supported input formats:

- JSON (`.json`)
- YAML (`.yml`, `.yaml`)

Supported output formats:

- `stylish` — human-readable tree view (default)
- `plain` — line-by-line change descriptions
- `json` — structured JSON output

---

## Requirements

- Python 3.12+
- pip (recommended) or any modern Python package manager

---

## Installation

### From PyPI (when published)

```bash
pip install gendiff
```

From source (recommended for development)

```bash
git clone https://github.com/chifcrow/python-project-50.git
cd python-project-50
python -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

After installation, the gendiff command becomes available.

## Usage

### CLI

Help:

```bash
gendiff -h
```

Compare two files (default format is stylish):

```bash
gendiff file1.json file2.yml
```

Explicit format:

```bash
gendiff --format plain file1.yml file2.yml
gendiff --format json file1.json file2.json
```

## Library

```python
from gendiff import generate_diff

diff = generate_diff(
    "path/to/file1.yml",
    "path/to/file2.yml",
    format_name="plain",
)

print(diff)
```

## Examples

### 1. Comparing flat JSON files (default `stylish` format)

Shows basic comparison of two flat JSON configuration files.

[![asciicast](https://asciinema.org/a/95vuwhnFQpMBpX9ZA93JRVC9g.svg)](https://asciinema.org/a/95vuwhnFQpMBpX9ZA93JRVC9g)

---

### 2. Comparing nested YAML files (`stylish` format)

Demonstrates recursive diff for nested configuration structures.

[![asciicast](https://asciinema.org/a/QaNEwRPPWz5iM1QK79cBO5G0v.svg)](https://asciinema.org/a/QaNEwRPPWz5iM1QK79cBO5G0v)

---

### 3. Different output formats (`plain` and `json`)

Shows alternative output formats suitable for logs or machine processing.

[![asciicast](https://asciinema.org/a/4ljQRx9Kv8mzEs6PSWsGpHrVu.svg)](https://asciinema.org/a/4ljQRx9Kv8mzEs6PSWsGpHrVu)

[![asciicast](https://asciinema.org/a/8pGzb4Xn5Tuk1Bvzb9MVzdnQk.svg)](https://asciinema.org/a/8pGzb4Xn5Tuk1Bvzb9MVzdnQk)

## Development

Lint:

```bash
make lint
```

Auto-fix lint issues:

```bash
make lint-fix
```

Run tests:

```bash
make test
```

Run tests with coverage.xml generation:

```bash
make test-coverage
```

## Project Structure

```text
gendiff/
├── __init__.py
├── gendiff.py
├── parser.py
├── diff_builder.py
├── formatters/
│   ├── __init__.py
│   ├── stylish.py
│   ├── plain.py
│   └── json.py
└── scripts/
    └── gendiff.py
tests/
└── test_data/
```

## Technologies

- Python 3.12+
- PyYAML
- pytest / pytest-cov
- Ruff
- GitHub Actions (CI)
- SonarCloud (quality & coverage)

## License

MIT
