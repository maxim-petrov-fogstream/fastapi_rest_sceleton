lint:
	black src
	isort -y
	flake8 --config=.flake8
	pylint src
