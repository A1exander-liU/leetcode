from typing import List


class Solution:
    """

    1 -> 2 -> 3
      -> 3 -> 2

    2 -> 1 -> 3
      -> 3 -> 1

    3 -> 1 -> 2
      -> 2 -> 1

    every step choose from remaining nums
    - how to efficiently determine which nums are available at current step
    - simple way is check if current value was already added

    choose 1
    - index 0, remaining: [2(1),3(2)]

    choose 2:
    - index 1, remaining: [1(0),3(2)]

    choose 1,2:
    - index 0,1, remaining: [3(2)]


    current to keep track of nums so far, start as []
    - everytime we iterate over all numbers and add first num that doesn't apper yet in current
      - if it appears in current that means we already added it (also the nums are unique as well)
    - when current is same size of the numbers we add current to result
      - since permutation is just rearrangment, size should not change
      - also it means we added all the different numbers in nums

    use set: more space but already have O(n) space
             - constant time check if num in current

    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        def permuteHelper(current: List[int], result: List[List[int]]) -> None:
            if len(current) == len(nums):
                result.append(current)
                return

            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                permuteHelper(current + [nums[i]], result)

        result = []
        permuteHelper([], result)

        return result
