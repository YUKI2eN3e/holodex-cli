set windows-shell := ["C:\\Program Files\\Git\\bin\\sh.exe", "-c"]

_default: tasks

_setup_poetry:
	poetry install

# SetUp project
setup: _setup_poetry
	poetry run pre-commit install

# Run ipython
ipython:
	poetry run ipython

# Organize imports
sort:
	poetry run isort --profile black --line-length 88 .

# Format code
format:
	poetry run black .

# Lint and format all files
lint:
	poetry check
	@just sort
	@just format

# List tasks
tasks:
	@just --list

# Build project
build: _setup_poetry
	poetry build

# Install program using pipx
install: build
	pipx install ./dist/`ls -t dist | head -n2 | grep whl`
	mkdir -p ~/.local/holodex-cli
	cp --update config.toml ~/.local/holodex-cli/config.toml

_uninstall:
	pipx uninstall holodex-cli

# Uninstall program using pipx
uninstall: _uninstall
	[ ! -e ~/.local/holodex-cli/config.toml || rm ~/.local/holodex-cli/config.toml ]
	rmdir ~/.local/holodex-cli 2> /dev/null

# Reinstall program using pipx
reinstall: _uninstall
	@just install

# Run cli program
run:
    poetry run holodex