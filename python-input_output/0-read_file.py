#!/usr/bin/python3
"""Read a file"""

def read_file(filename=""):
    """Reads a text file and prints it to stdout.

    Args:
        filename (str): Name of the file to read. If not provided,
        defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
