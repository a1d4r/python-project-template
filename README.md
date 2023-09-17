# Python Packages Project Generator

## TL;DR

```bash
cookiecutter gh:a1d4r/python-package-template --checkout master
```

> All you need is the latest version of cookiecutter 😉

## 🚀 Features

In this [cookiecutter 🍪](https://github.com/cookiecutter/cookiecutter) template we combine state-of-the-art libraries and best development practices for Python.

### Development features

- Supports `Python 3.9` and higher.
- [`Poetry`](https://python-poetry.org/) as a dependencies manager. See configuration in [`pyproject.toml`](https://github.com/a1d4r/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/pyproject.toml) and [`setup.cfg`](https://github.com/a1d4r/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/setup.cfg).
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort), [`autoflake`](https://github.com/myint/autoflake), and [`pyupgrade`](https://github.com/asottile/pyupgrade).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Ready-to-use [`.editorconfig`](https://github.com/a1d4r/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.editorconfig), [`.dockerignore`](https://github.com/a1d4r/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.dockerignore), and [`.gitignore`](https://github.com/a1d4r/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.gitignore). You don't have to worry about those things.

### Deployment features

- `Github Actions` with predefined [build workflow](https://github.com/a1d4r/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/workflows/build.yml) as the default CI/CD.
- `Gitlab CI`
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`](https://github.com/a1d4r/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile#L89). More details in [makefile-usage](#makefile-usage).
- [Dockerfile](https://github.com/a1d4r/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker/Dockerfile) for your package.

## 🤯 How to use it

### Installation

To begin using the template consider updating `cookiecutter`

```bash
pip install -U cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gh:a1d4r/python-package-template --checkout master
```

### Input variables

Template generator will ask you to fill some variables.

The input variables, with their default values:

|      **Parameter**       |                    **Default value**                    | **Description**                                                                                                                    |
|:------------------------:|:-------------------------------------------------------:|------------------------------------------------------------------------------------------------------------------------------------|
|      `project_name`      |                    `python-project`                     | [Check the availability of possible name](http://ivantomic.com/projects/ospnc/) before creating the project.                       |
|  `project_description`   |               based on the `project_name`               | Brief description of your project.                                                                                                 |
|      `git_platform`      |                        `github`                         | Git platform (Github/Gitlab)                                                                                                       |
|        `username`        |                       `username`                        | User or organization name for Git platform                                                                                         |
|      `git_repo_url`      | based on `git_platform`, `project_name` and `username`  | URL to the git repository                                                                                                          |
|         `email`          |               based on the `organization`               | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`.               |
|        `version`         |                         `0.1.0`                         | Initial version of the package. Make sure it follows the [Semantic Versions](https://semver.org/) specification.                   |
| `minimal_python_version` |                          `3.8`                          | Minimal Python version. One of `3.9`, `3.10`, `3.11`. It is used for builds, CI and formatters (`black`, `isort` and `pyupgrade`). |
|      `line_length`       |                           88                            | The max length per line (used for codestyle with `black` and `isort`). NOTE: This value must be between 50 and 300.                |

All input values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. 😉

#### Demo

[![Demo of github.com/TezRomacH/python-package-template](https://asciinema.org/a/422052.svg)](https://asciinema.org/a/422052)

### More details

Your project will contain `README.md` file with instructions for development, deployment, etc. You can read [the project README.md template](https://github.com/a1d4r/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D) before.

### Initial set up

#### Initialize `poetry`

By running `make install`

After you create a project, it will appear in your directory, and will display [a message about how to initialize the project](https://github.com/a1d4r/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D#very-first-steps).

#### Initialize `pre-commit`

By running `make pre-commit-install`. Make sure to set up git first via `git init`.


### Makefile usage

[`Makefile`](https://github.com/a1d4r/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile) contains a lot of functions for faster development.

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

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort`, `autoflake`, and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black`, and `darglint` library

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
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
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
make test && make check-codestyle && make mypy && make check-safety
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

More information [about docker](https://github.com/a1d4r/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker).

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

## 🏅 Acknowledgements

This template was initially forked from the following template:

- [🚀 Your next Python package needs a bleeding-edge project structure.](https://github.com/TezRomacH/python-package-template)
