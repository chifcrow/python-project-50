PORT ?= 8000

install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

coverage-missing:
	poetry run pytest --cov-report=term-missing --cov=gendiff

lint:
	poetry run ruff check gendiff tests

lint-fix:
	poetry run ruff check gendiff tests --fix

check:
	$(MAKE) selfcheck
	$(MAKE) test
	$(MAKE) lint

build:
	poetry build

draw:
	poetry run draw

selfcheck:
	poetry check

amend-and-push:
	git add .
	git commit --amend --no-edit
	git push --force

dev:
	poetry run flask --app gendiff:app run

start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) gendiff:app

ALL:
	$(MAKE) lint
	$(MAKE) install
	$(MAKE) coverage-missing
	$(MAKE) build
	$(MAKE) package-install
	$(MAKE) test
