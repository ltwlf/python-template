"""Main entry point for the mypackage module."""

from . import add, greet


def main() -> None:
    """Main function demonstrating package functionality."""
    result = add(2, 3)
    print(f"2 + 3 = {result}")
    print(greet("World"))


if __name__ == "__main__":
    main()
