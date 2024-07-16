import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) == k and num > heap[0]:
                heapq.heapreplace(heap, num)
            elif len(heap) < k:
                heapq.heappush(heap, num)

        return heap[0]
