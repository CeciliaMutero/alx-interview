#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists of integers."""
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(n - 1):
        row = [1]
        for i in range(len(triangle[-1]) - 1):
            row.append(triangle[-1][i] + triangle[-1][i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
