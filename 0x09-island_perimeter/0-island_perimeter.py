#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Arguments:
    grid -- list of list of integers where:
            - 0 represents water
            - 1 represents land
            - Cells are connected horizontally/vertically (not diagonally)
            - The grid is surrounded by water and contains one island

    Returns:
    The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 1
                if r < rows - 1 and grid[r+1][c] == 1:
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 1
                if c < cols - 1 and grid[r][c+1] == 1:
                    perimeter -= 1

    return perimeter
