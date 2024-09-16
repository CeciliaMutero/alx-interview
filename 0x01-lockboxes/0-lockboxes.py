#!/usr/bin/python3
"""Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes can be opened"""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    queue = [0]
    while queue:
        """checks every box"""
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)
    return all(opened)
