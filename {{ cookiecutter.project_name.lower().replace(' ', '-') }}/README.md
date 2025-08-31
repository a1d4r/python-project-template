# {{ cookiecutter.project_name.replace('-', ' ').replace('_', ' ') }}

## Installation

1. Clone `git` repo:

```bash
git clone {{ cookiecutter.git_repo_url }}.git
cd {{ cookiecutter.project_name.lower().replace(' ', '-') }}
```

2. If you don't have `uv` installed run:

```bash
make uv-download
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
make pre-commit-install
```

4. Run formatters, linters, and tests. Make sure there is no errors.

```bash
make format lint test
```

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

## Credits

This project was generated with [`python-package-template`](https://github.com/a1d4r/python-package-template)
