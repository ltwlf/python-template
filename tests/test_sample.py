"""Simple tests for the example package."""

from src.mypackage import add, greet


def test_add() -> None:
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0


def test_greet() -> None:
    """Test the greet function."""
    assert greet("World") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"
