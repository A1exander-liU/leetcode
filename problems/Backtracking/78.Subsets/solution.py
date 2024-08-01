from typing import List


class Solution:
    """
    2 3 5 target: 8

    []  -> 2 -> 2 -> 2 -> 2 -> 8 [2,2,2,2]
                       -> 3 -> x
                       -> 5 -> x
                  -> 3 -> 2 -> x
                       -> 3 -> x
                       -> 5 -> x
             -> 3 -> 2 -> 2 -> x
                  -> 3 -> 8 [2,3,3]
                  -> 5 -> x
        -> 3 -> 2 -> 2 -> 2 -> x
                  -> 3 -> 8 [3,2,3]
             -> 5 -> 8 [3,5]

    - [2,3,5]
    - [5,3,2]
    3 appears before 2 in candidates so unique combo of 2,2,3 appears as 3,2,2 first

    - 2 -> 2 -> 3 before 2 -> 3 -> 2

    -> 3 -> 2 -> 2 before 2 -> 2 -> 3

    backtracking
    3 -> 2 -> 2 -> 7 [3,2,2]
    ...
    2 -> 2 -> 2 -> x
           -> 3 -> 7 [2,2,3] how to detect this

    must start at same number since each candidate can be reused as many times
    - so must try everything but need to know if we have dupe when we found another combo
    - freq map since candiates are 2 - 40, array of size 41 (0-40)
    - all dupes are grouped together so only need to keep track of current group
    - when adding a new combo: update it as current group to track for dupes

    2 -> 2 -> 2 -> 2

    2 -> 3 -> 2
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinationSumHelper(
            start: int, currentSum: int, currentNums: List[int], result: List[List[int]]
        ) -> None:
            if currentSum == target:
                result.append(currentNums)
                return
            elif currentSum > target:
                currentNums.pop()
                return

            for i in range(0, len(candidates)):
                if i < start:
                    continue
                combinationSumHelper(
                    i, currentSum + candidates[i], currentNums + [candidates[i]], result
                )

        result = []
        combinationSumHelper(0, 0, [], result)

        return result
