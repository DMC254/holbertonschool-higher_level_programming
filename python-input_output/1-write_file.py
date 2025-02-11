#!/usr/bin/python3
"""Define a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file.

    Args:
        filename (str): The name of the file to write to. Defaults to empty string.
        text (str): The string to write to the file.
    """

    with open(filename, "w", encoding="utf-8") as f:
        w_content = f.write(text)
    return w_content
