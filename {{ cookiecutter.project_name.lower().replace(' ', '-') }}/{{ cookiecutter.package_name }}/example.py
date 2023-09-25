"""Example of code."""


def hello(name: str) -> str:
    """Just a greetings example.

    >>> hello("World")
    'Hello World!'
    """
    return f"Hello {name}!"


if __name__ == "__main__":
    print(hello("World"))  # noqa: T201
