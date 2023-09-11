# https://leetcode.com/problems/number-of-islands/
from collections import deque


def num_islands(grid: list[list[str]]) -> int:
    rows, columns = len(grid), len(grid[0])
    number_of_islands = 0
    visited_indexes = set()  # (row, column)

    def bfs(r: int, c: int):
        queue = deque()
        visited_indexes.add((r, c))
        queue.append((r, c))
        while queue:
            row, col = queue.pop()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = row + dr, dc + col
                visited_indexes.add((r, c))
                if grid[r][c] == "1" and (r, c) not in visited_indexes and r < rows and c < columns:
                    queue.append((r, c))
                    visited_indexes.add((r, c))

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == "1" and (r, c) not in visited_indexes:
                bfs(r, c)
                number_of_islands += 1

    return number_of_islands
