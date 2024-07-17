
local-setup:
	pyenv shell 3.10.0
	pip install poetry=="1.8.3"
	poetry shell
	# install libraries from the lockfile.
	poetry install


test:
	python -m pytest