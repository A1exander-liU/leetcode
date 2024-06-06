from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)

        prev_smallest = [-1] * n
        next_smallest = [n] * n

        for i in range(1, n, 1):
            p = i - 1

            while p >= 0 and heights[p] >= heights[i]:
                p = prev_smallest[p]
            prev_smallest[i] = p

        for i in range(n - 2, -1, -1):
            s = i + 1

            while s < n and heights[s] >= heights[i]:
                s = next_smallest[s]
            next_smallest[i] = s

        for i in range(n):
            area = max(area, heights[i] * (next_smallest[i] - prev_smallest[i] - 1))

        return area
