#!/usr/bin/python3
"""Define inherited list class MyList."""


class MyList(list):
    """Implement sorted print for built-in list class."""

    def print_sorted(self):
        """Print list in sorted and ascending order."""
        print(sorted(self))
