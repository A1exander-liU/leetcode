from typing import List, Tuple, Set
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def outOfBounds(pos: Tuple[int, int]) -> bool:
            return (
                pos[0] < 0
                or pos[1] < 0
                or pos[0] >= len(grid)
                or pos[1] >= len(grid[0])
            )

        def bfs(start: Tuple[int, int], visited: Set[Tuple[int, int]]) -> int:
            area = 0
            q = deque()
            q.append(start)

            while len(q) > 0:
                area += 1
                node = q.popleft()
                neighbors = [
                    (node[0] - 1, node[1]),
                    (node[0], node[1] + 1),
                    (node[0] + 1, node[1]),
                    (node[0], node[1] - 1),
                ]
                for neighbor in neighbors:
                    if outOfBounds(neighbor) or grid[neighbor[0]][neighbor[1]] == 0:
                        continue
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            return area

        maxArea = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and (i, j) not in visited:
                    visited.add((i, j))
                    area = bfs((i, j), visited)
                    maxArea = max(maxArea, area)

        return maxArea
