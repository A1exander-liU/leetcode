from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def subsetsWithDupHelper(pos: int, current: List[int], result: List[List[int]]) -> None:
            for i in range(pos, len(nums)):
                newSubset = current + [nums[i]]
                if (i > 1 and nums[i - 2] != nums[i - 1] and nums[i - 1] == nums[i]) or (i > 0 and nums[0] != nums[i - 1] and nums[i - 1] == nums[i]):
                    continue
                result.append(newSubset)
                subsetsWithDupHelper(i + 1, newSubset, result)


        result = [[]]
        subsetsWithDupHelper(0, [], result)

        return result


s = Solution()
result = s.subsetsWithDup([1,2,2])
"""
1 4 4 4 4
"""

print(result)
