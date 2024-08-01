from typing import List, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n == 2 or n == 3:
            return []

        def validChoices(row: int, queens: List[Tuple[int, int]]) -> List[int]:
            valid = []

            diagonals = set()
            cols = set()

            for queen in queens:
                cols.add(queen[1])
                diff = row - queen[0]
                diagonals.add((queen[0] + diff, queen[1] + diff))
                diagonals.add((queen[0] + diff, queen[1] - diff))

            for col in range(n):
                if col in cols:
                    continue
                if (row, col) in diagonals:
                    continue
                valid.append(col)

            return valid

        def solveNQueensHelper(
            pos: Tuple[int, int],
            row: int,
            queens: List[Tuple[int, int]],
            validCols: List[int],
            board: List[List[str]],
            result: List[List[str]],
        ) -> None:
            if row == n:
                result.append(["".join(r) for r in board])
                board[pos[0]][pos[1]] = "."
                return

            if not validCols:
                board[pos[0]][pos[1]] = "."
                return

            for col in validCols:
                newQueens = queens + [(row, col)]

                board[row][col] = "Q"
                solveNQueensHelper(
                    (row, col),
                    row + 1,
                    newQueens,
                    validChoices(row + 1, newQueens),
                    board,
                    result,
                )

            board[pos[0]][pos[1]] = "."

        board = [["." for _ in range(n)] for _ in range(n)]
        result = []
        solveNQueensHelper(
            pos=(0, 0),
            row=0,
            queens=[],
            validCols=[col for col in range(n)],
            board=board,
            result=result,
        )

        return result

