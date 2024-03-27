"""This module is called before project is created."""

import re
import sys

PACKAGE_NAME = "{{ cookiecutter.package_name }}"
LINE_LENGTH_PARAMETER = "{{ cookiecutter.line_length }}"

MODULE_REGEX = re.compile(r"^[a-z][a-z0-9\-\_]+[a-z0-9]$")
SEMVER_REGEX = re.compile(
    r"""
        ^
        (?P<major>0|[1-9]\d*)
        \.
        (?P<minor>0|[1-9]\d*)
        \.
        (?P<patch>0|[1-9]\d*)
        (?:-(?P<prerelease>
            (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
            (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
        ))?
        (?:\+(?P<build>
            [0-9a-zA-Z-]+
            (?:\.[0-9a-zA-Z-]+)*
        ))?
        $
    """,
    re.VERBOSE,
)


def validate_package_name(package_name: str) -> None:
    """Ensure that `package_name` parameter is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.

    Args:
        package_name: current project name

    Raises:
        ValueError: If project_name is not a valid Python module name
    """
    if MODULE_REGEX.fullmatch(package_name) is None:
        message = f"ERROR: The package name `{package_name}` is not a valid Python module name."
        raise ValueError(message)


def validate_line_length(line_length: int) -> None:
    """Validate line_length parameter. Length should be between 50 and 300.

    Args:
        line_length: integer parameter for ruff formatters

    Raises:
        ValueError: If line_length isn't between 50 and 300
    """
    if not (50 <= line_length <= 300):
        message = f"ERROR: line_length must be between 50 and 300. Got `{line_length}`."
        raise ValueError(message)


def main() -> None:
    try:
        validate_package_name(package_name=PACKAGE_NAME)
        validate_line_length(line_length=int(LINE_LENGTH_PARAMETER))
    except ValueError as ex:
        print(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()
