import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (point[0] ** 2 + point[1] ** 2, point))

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
