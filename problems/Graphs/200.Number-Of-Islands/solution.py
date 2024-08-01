from typing import List, Set, Tuple
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def outOfBounds(i: int, j: int) -> bool:
            return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])

        def bfs(start: Tuple[int, int], visited: Set[Tuple[int, int]]) -> None:
            q = deque()
            q.append(start)

            while len(q) > 0:
                iterations = len(q)

                for _ in range(iterations):
                    node = q.popleft()
                    neighbors: List[Tuple[int, int]] = [
                        (node[0] - 1, node[1]),
                        (node[0], node[1] + 1),
                        (node[0] + 1, node[1]),
                        (node[0], node[1] - 1),
                    ]
                    for neighbor in neighbors:
                        i, j = neighbor
                        if outOfBounds(i, j) or grid[i][j] == "0":
                            continue
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)

        islandCount = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    bfs((i, j), visited)
                    islandCount += 1

        return islandCount

