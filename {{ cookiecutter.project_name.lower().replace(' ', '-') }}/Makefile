#* Variables
SHELL := /usr/bin/env bash
PYTHON := python3

#* Docker variables
IMAGE := {{ cookiecutter.project_name.lower().replace(' ', '-') }}
VERSION := latest

#* Directories with source code
CODE = {{ cookiecutter.package_name }} tests
TESTS = tests

#* Poetry
.PHONY: poetry-download
poetry-download:
	curl -sSL https://install.python-poetry.org | $(PYTHON) -

.PHONY: poetry-remove
poetry-remove:
	curl -sSL https://install.python-poetry.org | $(PYTHON) - --uninstall

#* Installation
.PHONY: install
install:
	poetry lock --no-interaction --no-update
	poetry install --no-interaction --sync

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

#* Formatters
.PHONY: codestyle
codestyle:
	poetry run ruff check $(CODE) --fix-only
	poetry run black --config pyproject.toml $(CODE)

.PHONY: format
format: codestyle

#* Test
.PHONY: test
test:
	poetry run coverage run
	poetry run coverage report
	poetry run coverage xml

# Validate pyproject.toml
.PHONY: check-poetry
check-poetry:
	poetry check

#* Check code style
.PHONY: check-black
check-black:
	poetry run black --diff --check --config pyproject.toml $(CODE)

.PHONY: check-codestyle
check-codestyle: check-black

#* Static linters

.PHONY: check-ruff
check-ruff:
	poetry run ruff check $(CODE) --no-fix

.PHONY: check-mypy
check-mypy:
	poetry run mypy --install-types --non-interactive --config-file pyproject.toml $(CODE)

.PHONY: static-lint
static-lint: check-ruff check-mypy

#* Check safety

.PHONY: check-safety
check-safety:
	poetry run safety check --full-report

.PHONY: lint
lint: check-poetry check-codestyle static-lint

.PHONY: update-dev-deps
update-dev-deps:
	poetry add -G dev black@latest mypy@latest pre-commit@latest pytest@latest \
										coverage@latest safety@latest typeguard@latest ruff@latest

#* Docker
# Example: make docker-build VERSION=latest
# Example: make docker-build IMAGE=some_name VERSION=0.1.0
.PHONY: docker-build
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build -t $(IMAGE):$(VERSION) .

# Example: make docker-remove VERSION=latest
# Example: make docker-remove IMAGE=some_name VERSION=0.1.0
.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

.PHONY: docker-up
docker-up:
	docker compose up

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove:
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: ruffcache-remove
ruffcache-remove:
	find . | grep -E ".ruff_cache" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: reports-remove
reports-remove:
	rm -rf reports/

.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove ruffcache-remove \
ipynbcheckpoints-remove pytestcache-remove reports-remove
