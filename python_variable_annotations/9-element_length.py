#!/usr/bin/env python3
"""Module defines a function which returns length of iterable elements."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples (element, length) for each sequence in lst."""
    return [(i, len(i)) for i in lst]
