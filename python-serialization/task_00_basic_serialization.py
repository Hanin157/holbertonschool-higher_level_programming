#!/usr/bin/env python3
"""
task_00_basic_serialization.py

Basic serialization:
- serialize a Python dictionary into a JSON file
- deserialize a JSON file back into a Python dictionary
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): output JSON filename (replaces file if exists)
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")
    if not isinstance(filename, str) or not filename:
        raise ValueError("filename must be a non-empty string")

    # 'w' replaces the file content if it already exists
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): input JSON filename

    Returns:
        dict: deserialized JSON data as a Python dictionary
    """
    if not isinstance(filename, str) or not filename:
        raise ValueError("filename must be a non-empty string")

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("JSON content is not a dictionary")

    return data
