#!/usr/bin/python3
"""calculate rain"""


def rain(walls):
    """calculate rain"""
    total = 0
    i = 0
    start = None
    end = None
    limit = len(walls)
    while i < limit:
        if start is not None and end is not None:
            size = end - start - 1
            total = total + (min([walls[start], walls[end]]) * size)
            start = None
            end = None
        if start is None and walls[i] > 0:
            start = i

            i = i + 1
            continue
        if start is not None and walls[i] > 0:
            end = i
            continue
        i = i+1
    return total
