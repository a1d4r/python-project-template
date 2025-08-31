# Python Packages Project Generator

## TL;DR

```bash
cookiecutter gh:a1d4r/python-project-template --checkout main
```

## Features

In this [cookiecutter 🍪](https://github.com/cookiecutter/cookiecutter) template we combine state-of-the-art libraries
and best development practices for Python.

### Development features

- Supports `Python 3.9 - 3.13`
- [`uv`](https://docs.astral.sh/uv/) as a package manager.
- Automatic codestyle with [`ruff formatter`](https://docs.astral.sh/ruff/formatter/)
- Linting with [`ruff`](https://github.com/astral-sh/ruff)
- Type checks with [`mypy`](https://mypy.readthedocs.io), security checks
  with [`safety`](https://github.com/pyupio/safety).
- Dependencies check with [`deptry`](https://deptry.com/)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/) and [`coverage`](https://github.com/nedbat/coveragepy).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Ready-to-use [`.editorconfig`](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/.editorconfig), [`.dockerignore`](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/.dockerignore), and [`.gitignore`](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/.gitignore).

### Deployment features

- `Github Actions` with linters and tests in
  the [workflow](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/.github/workflows/%7B%7B%20cookiecutter.package_name%20%7D%7D.yml).
- `Gitlab CI` with linters and tests in
  the [pipeline](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/.gitlab-ci.yml).
  Click [here](pages/gitlab.md) for a detailed overview.
- Ready-to-use [`Makefile`](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/Makefile) with
  formatting, linting, and testing. More details in [makefile-usage](#makefile-usage).
- [Dockerfile](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/Dockerfile) for your package.
- [docker-compose.yml](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/docker-compose.yml) for
  local development in Docker.

## How to use it

### Installation

To begin using the template consider updating `cookiecutter`

```bash
pip install -U cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gh:a1d4r/python-project-template --checkout master
```

### Input variables

Template generator will ask you to fill some variables.

The input variables, with their default values:

|   **Parameter**    |                   **Default value**                    | **Description**                                                                                              |
|:------------------:|:------------------------------------------------------:|--------------------------------------------------------------------------------------------------------------|
|   `project_name`   |                    `python-project`                    | [Check the availability of possible name](http://ivantomic.com/projects/ospnc/) before creating the project. |
|   `package_name`   |              based on the `project_name`               | Name of the python package with source code                                                                  |
|   `git_platform`   |                        `github`                        | Git platform (Github/Gitlab)                                                                                 |
|     `username`     |                       `username`                       | User or organization name for Git platform                                                                   |
|   `git_repo_url`   | based on `git_platform`, `project_name` and `username` | URL to the git repository                                                                                    |
|  `python_version`  |                         `3.9`                          | Python version. One of `3.9`, `3.10`, `3.11`, `3.12`, `3.13`. It is used for builds, CI and formatters.      |
|   `line_length`    |                           88                           | The max length per line. Must be between 50 and 300.                                                         |
| `install_pydantic` |                          true                          | If `pydantic` with `mypy` plugin should be installed                                                         |

All input values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. 😉

### More details

Your project will contain `README.md` file with instructions for development, deployment, etc. You can
read [the project README.md template](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/README.md)
before.

### Initial set up

#### Initialize `uv`

By running `make install`

After you create a project, it will appear in your directory, and will
display [a message about how to initialize the project](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/README.md#installation).

#### Initialize `pre-commit`

By running `make pre-commit-install`. Make sure to set up git first via `git init`.

### Makefile usage

[`Makefile`](%7B%7B%20cookiecutter.project_name.lower().replace('%20',%20'-')%20%7D%7D/Makefile)
contains a lot of functions
for faster development.

<details>
<summary>1. Download uv</summary>
<p>

To download and install uv run:

```bash
make uv-install
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

Automatic formatting uses `ruff` formatter

```bash
make codestyle

# or use synonym
make format
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

Update all libraries to the latest version using one command

```bash
make update
```

</p>
</details>

<details>
<summary>4. Code security</summary>
<p>

This command identifies security issues with `Safety`

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

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

Run with docker compose

```bash
make docker-up
```

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete cache and build files:

```bash
make cleanup
```

</p>
</details>

## 🏅 Acknowledgements

This template was initially forked from the following template:

- [🚀 Your next Python package needs a bleeding-edge project structure.](https://github.com/TezRomacH/python-package-template)
