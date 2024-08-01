from typing import List


class Solution:
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

            for i in range(start, len(candidates)):
                combinationSumHelper(
                    i, currentSum + candidates[i], currentNums + [candidates[i]], result
                )

        result = []
        combinationSumHelper(0, 0, [], result)

        return result
