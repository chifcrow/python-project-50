lint:
	ruff check gendiff tests

lint-fix:
	ruff check gendiff tests --fix

test:
	pytest

test-coverage:
	pytest --cov=gendiff --cov-report=xml

coverage-missing:
	pytest --cov=gendiff --cov-report=term-missing

check:
	$(MAKE) test
	$(MAKE) lint
