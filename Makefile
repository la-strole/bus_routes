install:

	# Install poetry
	curl -sSL https://install.python-poetry.org | python3 -

	# Install poetry dependencies
	~/.local/bin/poetry install --no-root

run:
	~/.local/bin/poetry run python main.py
	