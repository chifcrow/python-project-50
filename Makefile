lint:
	flake8 .

test:
	pytest

coverage:
	coverage run -m pytest
	coverage report
	coverage xml
