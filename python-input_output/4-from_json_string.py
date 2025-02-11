#!/usr/bin/puthon3
"""Define a function that returns an obj
(Python data structure) represented by a JSON string"""

import json


def from_json_string(my_str):
    """Return an object(Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to parse.

    Returns:
        object: The parsed object.
    """
    return json.loads(my_str)
