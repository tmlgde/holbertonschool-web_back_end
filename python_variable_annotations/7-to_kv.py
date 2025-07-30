#!/usr/bin/env python3
"""Module that defines a function to return a key and the square of a value as a tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of v as a float."""
    return (k, float(v ** 2))
