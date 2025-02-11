#!/usr/bin/python3
"""Define a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty
        string.
        text (str): The string to append to the file. Defaults to an empty
        string.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
