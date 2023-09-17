"""This module is called after project is created."""
import textwrap
from pathlib import Path

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"

# Values to generate Git repository
GIT_REPO_URL = "{{ cookiecutter.git_repo_url }}"
GIT_PLATFORM = "{{ cookiecutter.git_platform }}"


def print_further_instructions(project_name: str, git_repo_url: str) -> None:
    """Show user what to do next after project creation.

    Args:
        project_name: current project name
        git_repo_url: Git repository URL
    """
    project_directory = project_name.lower().replace(" ", "-")

    message = f"""
    Your project {project_name} is created.

    1) Now you can start working on it:

        $ cd {project_directory} && git init

    2) If you don't have Poetry installed run:

        $ make poetry-download

    3) Initialize poetry and install pre-commit hooks:

        $ make install
        $ make pre-commit-install

    4) Run formatters, linters, and tests:

        $ make format lint test

    5) Upload initial code to GitHub:

        $ git add .
        $ git commit -m "Initial commit"
        $ git branch -M main
        $ git remote add origin {git_repo_url}.git
        $ git push -u origin main
    """
    print(textwrap.dedent(message))


def rm_tree(pth: Path):
    for child in pth.iterdir():
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()


def remove_unrelated_ci_configuration(
    project_directory: Path,
    git_platform: str,
) -> None:
    if git_platform == "github":
        (project_directory / ".gitlab-ci.yml").unlink()
    elif git_platform == "gitlab":
        rm_tree(project_directory / ".github")
    else:
        raise ValueError(f"Unsupported git platform: {git_platform}")


def main() -> None:
    print_further_instructions(project_name=PROJECT_NAME, git_repo_url=GIT_REPO_URL)
    remove_unrelated_ci_configuration(
        project_directory=PROJECT_DIRECTORY,
        git_platform=GIT_PLATFORM,
    )


if __name__ == "__main__":
    main()
