from typing import List, Tuple, Set
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def outOfBounds(i: int, j: int) -> bool:
            return i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0])

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set(starts)
            q = deque(starts)
            validCells = set(starts)

            while len(q) > 0:
                cell = q.popleft()

                neighbors = [
                    (cell[0] - 1, cell[1]),
                    (cell[0], cell[1] - 1),
                    (cell[0] + 1, cell[1]),
                    (cell[0], cell[1] + 1),
                ]

                for neighbor in neighbors:
                    i, j = neighbor

                    if outOfBounds(i, j) or neighbor in visited:
                        continue

                    if heights[i][j] >= heights[cell[0]][cell[1]]:
                        validCells.add(neighbor)
                        q.append(neighbor)
                        visited.add(neighbor)

            return validCells

        pacificEdge = [
            (i, j)
            for i in range(len(heights))
            for j in range(len(heights[i]))
            if i == 0 or j == 0
        ]
        atlanticEdge = [
            (i, j)
            for i in range(len(heights))
            for j in range(len(heights[i]))
            if i == len(heights) - 1 or j == len(heights[i]) - 1
        ]

        canReachPacificPositions = bfs(pacificEdge)
        canReachAtlanticPositions = bfs(atlanticEdge)

        result = []
        for pos in canReachPacificPositions:
            if pos not in canReachAtlanticPositions:
                continue
            result.append(list(pos))

        return result
