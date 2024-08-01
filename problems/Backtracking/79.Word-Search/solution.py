from typing import List, Tuple


class Solution:
    pass


def dfs(board: List[List[str]], word: str) -> None:
    def findStartPositions() -> List[Tuple[int, int]]:
        positions = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != word[0]:
                    continue
                positions.append((i, j))

        return positions

    def dfsHelper(pos: Tuple[int, int], wordIndex: int, result: List[bool]) -> None:
        def findNextPositions(
            pos: Tuple[int, int], prevPos: Tuple[int, int] | None, wordIndex: int
        ) -> List[Tuple[int, int]]:
            i, j = pos
            # [up, right, down, left]
            positions = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
            validPositions = []
            for position in positions:
                i, j = position

                if (i < 0 or i >= len(board)) or (j < 0 or j >= len(board[0])):
                    continue
                if prevPos and position == prevPos:
                    continue
                if board[i][j] != word[wordIndex]:
                    continue
                validPositions.append(position)

            return validPositions

        i, j = pos

        if board[i][j] == word[wordIndex]:
            wordIndex += 1

        if wordIndex == len(word):
            result[0] = True
            return

        print(pos, wordIndex)

        positions = findNextPositions(pos=pos, prevPos=pos, wordIndex=wordIndex)
        for position in positions:
            dfsHelper(pos=position, wordIndex=wordIndex, result=result)

        return

    startingPositions = findStartPositions()
    result = [False]
    for position in startingPositions:
        print("===== start ======")
        dfsHelper(pos=position, wordIndex=0, result=result)
        print(result[0])


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]


print(sorted("dsa"))
