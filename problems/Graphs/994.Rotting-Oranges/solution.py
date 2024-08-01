from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def outOfBounds(i: int, j: int) -> bool:
            return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])

        def bfs(q: Deque[Tuple[int, int]], freshCount: int) -> int:
            visited = set()
            minutes = 0
            orangesRotted = 0

            while orangesRotted != freshCount and len(q) > 0:
                count = len(q)

                for _ in range(count):
                    tile = q.popleft()
                    visited.add(tile)
                    neighbors = [
                        (tile[0] - 1, tile[1]),
                        (tile[0], tile[1] + 1),
                        (tile[0] + 1, tile[1]),
                        (tile[0], tile[1] - 1),
                    ]

                    for neighbor in neighbors:
                        i, j = neighbor

                        if outOfBounds(i, j) or grid[i][j] == 0 or grid[i][j] == 2:
                            continue
                        if neighbor in visited:
                            continue

                        orangesRotted += 1
                        grid[i][j] = 2
                        q.append(neighbor)
                        visited.add(neighbor)

                minutes += 1

            if orangesRotted == freshCount:
                return minutes
            else:
                return -1

        freshCount = 0
        rotten = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        return bfs(rotten, freshCount)
