from typing import List, Set, Tuple
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def edgeCell(i: int, j: int) -> bool:
            return i == 0 or j == 0 or i == len(board) - 1 or j == len(board[i]) - 1

        def outOfBounds(i: int, j: int) -> bool:
            return i < 0 or i >= len(board) or j < 0 or j >= len(board[0])

        def bfs(
            start: Tuple[int, int], visited: Set[Tuple[int, int]], capture: bool = False
        ) -> None:
            q = deque([start])

            while len(q) > 0:
                cell = q.popleft()
                if capture:
                    board[cell[0]][cell[1]] = "X"

                neighbors = [
                    (cell[0] - 1, cell[1]),
                    (cell[0], cell[1] + 1),
                    (cell[0] + 1, cell[1]),
                    (cell[0], cell[1] - 1),
                ]

                for neighbor in neighbors:
                    i, j = neighbor

                    if outOfBounds(i, j) or neighbor in visited or board[i][j] == "X":
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)

            return

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i, j) in visited or board[i][j] == "X" or not edgeCell(i, j):
                    continue
                visited.add((i, j))
                bfs((i, j), visited)

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                if (i, j) in visited or board[i][j] == "X":
                    continue
                visited.add((i, j))
                bfs((i, j), visited, capture=True)

        return
