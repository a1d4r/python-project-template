# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Getting started

### Initialize your code

1. Initialize `git` inside your repo:

```bash
cd {{ cookiecutter.project_name }} && git init
```

2. If you don't have `Poetry` installed run:

```bash
make poetry-download
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
make pre-commit-install
```

4. Run formatters, linters, and tests

```bash
make format lint test
```

5. Upload initial code to GitHub:

```bash
git add .
git commit -m "Initial commit"
git branch -M master
git remote add origin {{ cookiecutter.git_repo_url }}.git
git push -u origin master
```

## Installation

```bash
poetry add {{ cookiecutter.project_name }}
```

### Makefile usage

[`Makefile`]({{ cookiecutter.git_repo_url }}/blob/master/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks could be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make format
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one comand

```bash
make update-dev-deps
```

</p>
</details>

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-security
```

This command identifies security issues with `Safety` and `Bandit`.

```bash
make check-security
```

To validate `pyproject.toml` use
```bash
make check-poetry
```

</p>
</details>

<details>
<summary>5. Linting and type checks</summary>
<p>

Run static linting with `pylint` and `mypy`:

```bash
make static-lint
```

</p>
</details>

<details>
<summary>6. Tests with coverage</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make static-lint && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker]({{ cookiecutter.git_repo_url }}/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## Credits

This project was generated with [`python-package-template`](https://github.com/a1d4r/python-package-template)
