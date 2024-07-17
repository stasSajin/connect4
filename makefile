
local-setup:
	pip install poetry=="1.8.3"
	poetry shell
	# install libraries from the lockfile.
	poetry install


test:
	python -m pytest -v