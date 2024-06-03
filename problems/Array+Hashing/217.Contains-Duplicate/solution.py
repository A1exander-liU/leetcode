from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = set()

        for num in nums:
            if num in counts:
                return True
            else:
                counts.add(num)

        return False
