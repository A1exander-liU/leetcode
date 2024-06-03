from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        current = { "val": "(", "left": None, "right": None, "opened": 1, "closed": 0 }

        while True:
            if current:
                stack.append(current)
                if current["opened"] + current["closed"] == n * 2:
                    result.append(current["val"])

                if current["opened"] < n:
                    current["left"] = { "val": current["val"] + "(", "left": None, "right": None, "opened": current["opened"] + 1, "closed": current["closed"] }
                
                if current["closed"] < current["opened"] and current["closed"] < n:
                    current["right"] = { "val": current["val"] + ")", "left": None, "right": None, "opened": current["opened"], "closed": current["closed"] + 1 }

                current = current["left"]
            elif stack:
                current = stack.pop()

                current = current["right"]
            else:
                break


        return result