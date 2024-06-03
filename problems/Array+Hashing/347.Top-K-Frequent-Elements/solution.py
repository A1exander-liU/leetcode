import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        counts_heap = []
        for num, count in counts.items():
            heapq.heappush(counts_heap, (-count, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(counts_heap)[1])

        return result


nums = [4, 1, 1, 1, 3, 3, 2, 2]
print(Solution().topKFrequent(nums, 2))
