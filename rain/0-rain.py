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
        last = 0
        if (i + 1) < (len(walls) - 1):
            last = walls[i + 1]
        if start is not None and end is not None:
            smallest = min([walls[start], walls[end]])
            for dent in range(start + 1, end):
                total = total + (smallest - walls[dent])
            start = None
            end = None
        if start is None and walls[i] > 0:
            start = i
            i = i + 1
            continue
        if start is not None and walls[i] > walls[i - 1] and walls[i] >= last:
            end = i
            continue
        i = i+1
    return total
