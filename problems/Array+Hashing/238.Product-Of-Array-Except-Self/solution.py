from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums)):
            result[i] *= product
            product *= nums[i]

        return result
