from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        stack = []

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                result[top] = i - top

            stack.append(i)

        return result
