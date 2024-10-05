from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        biggest = 0

        current = 1
        for i in range(len(nums) - 1):
            next = nums[i + 1]

            if nums[i] + 1 == next:
                current += 1
            else:
                if current > biggest:
                    biggest = current
                current = 1

        return max(biggest, current) if len(nums) > 0 else 0

