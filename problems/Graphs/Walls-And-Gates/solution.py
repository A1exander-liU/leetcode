from collections import deque
from typing import List, Tuple


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER = -1
        TREASURE = 0
        LAND = 2**31 - 1

        def outOfBounds(i: int, j: int) -> bool:
            return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])

        def bfs(start: Tuple[int, int]):
            visited = set([start])
            q = deque([(start[0], start[1], 0)])

            while len(q) > 0:
                row, col, distance = q.popleft()

                if grid[row][col] == TREASURE:
                    grid[start[0]][start[1]] = distance
                    return

                neighbors = [
                    (row - 1, col),
                    (row, col + 1),
                    (row + 1, col),
                    (row, col - 1),
                ]

                for neighbor in neighbors:
                    i, j = neighbor
                    if outOfBounds(i, j) or grid[i][j] == WATER or neighbor in visited:
                        continue

                    q.append((i, j, distance + 1))
                    visited.add(neighbor)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == LAND:
                    bfs((i, j))
