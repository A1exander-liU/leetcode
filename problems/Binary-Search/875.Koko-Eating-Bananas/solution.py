import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        k = right + 1

        while left <= right:
            new_k = left + (right - left) // 2

            eat_time = 0
            for pile in piles:
                eat_time += math.ceil(pile / new_k)

            if eat_time <= h:
                k = min(k, new_k)
                right = new_k - 1
            else:
                left = new_k + 1

        return k
