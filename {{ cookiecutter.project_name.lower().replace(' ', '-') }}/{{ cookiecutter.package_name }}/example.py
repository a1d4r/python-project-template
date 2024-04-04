"""Example of code."""
{% if cookiecutter.install_pydantic %}
import pydantic


class ExampleModel(pydantic.BaseModel):
    """Example model."""

    foo: str
    bar: int
{% endif %}

def hello(name: str) -> str:
    """Just a greetings example.

    >>> hello("World")
    'Hello World!'
    """
    return f"Hello {name}!"


if __name__ == "__main__":
    print(hello("World"))  # noqa: T201
