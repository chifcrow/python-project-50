lint:
	flake8 hexlet_code tests

test:
    pytest --cov=hexlet_code --cov-report=xml

coverage:
    bash <(curl -s https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64) after-build --exit-code $?