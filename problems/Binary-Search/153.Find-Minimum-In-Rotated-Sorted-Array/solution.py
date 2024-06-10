from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = 5001

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            min_val = min(min_val, nums[mid])

            # left side is sorted
            if nums[mid] > nums[left]:
                if nums[mid] < nums[right]:
                    min_val = min(min_val, nums[left])
                    right = mid - 1
                else:
                    left = mid + 1
            # right side is sorted
            else:
                if nums[right] < nums[max(0, mid - 1)]:
                    left = mid + 1
                else:
                    right = mid - 1

        return min_val
