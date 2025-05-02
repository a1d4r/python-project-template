#* Variables
SHELL := /usr/bin/env bash -o pipefail
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
	curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.5 $(PYTHON) -

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
	poetry run ruff format $(CODE)
	poetry run ruff check $(CODE) --fix-only

.PHONY: format
format: codestyle

#* Test
.PHONY: test
test:
	poetry run pytest
	poetry run coverage xml

# Validate dependencies
.PHONY: check-poetry
check-poetry:
	poetry check

.PHONY: check-deptry
check-deptry:
	poetry run deptry .

.PHONY: check-dependencies
check-dependencies: check-poetry check-deptry

#* Static linters

.PHONY: check-ruff
check-ruff:
	poetry run ruff check $(CODE) --no-fix
{% if cookiecutter.git_platform == 'gitlab' %}
.PHONY: check-ruff-gitlab
check-ruff-gitlab:
	poetry run ruff check $(CODE) --output-format=gitlab > ruff-report.json
{% endif %}
.PHONY: check-codestyle
check-codestyle:
	poetry run ruff format $(CODE) --check

.PHONY: check-mypy
check-mypy:
	poetry run mypy --install-types --non-interactive --config-file pyproject.toml $(CODE)
{% if cookiecutter.git_platform == 'gitlab' %}
.PHONY: check-mypy-gitlab
check-mypy-gitlab:
	poetry run mypy --install-types --non-interactive --no-error-summary --no-pretty --config-file pyproject.toml $(CODE) \
	2>&1 | poetry run mypy-gitlab-code-quality > mypy-report.json
{% endif %}
.PHONY: static-lint
static-lint: check-ruff check-mypy

#* Check safety

.PHONY: check-safety
check-safety:
	poetry run safety check --full-report

.PHONY: lint
lint: check-dependencies check-codestyle static-lint

.PHONY: update-dev-deps
update-dev-deps:
	poetry add -G dev mypy@latest pre-commit@latest pytest@latest deptry@latest \
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
