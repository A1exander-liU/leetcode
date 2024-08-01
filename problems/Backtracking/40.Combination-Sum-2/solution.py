from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def combinationSum2Helper(pos: int, current: int, currentNums: List[int], result: List[List[int]]) -> None:
            if current == target and currentNums not in result:
                result.append(currentNums)
                return
            elif current > target:
                currentNums.pop()
                return

            for i in range(pos, len(candidates)):
                combinationSum2Helper(i + 1, current + candidates[i], currentNums + [candidates[i]], result)

        result = []
        combinationSum2Helper(0, 0, [], result)

        return result


s = Solution()
testcases = [ { "candidates": [10, 1,2,7, 6,1,5], "target": 8 }, {"candidates": [2,5,1], "target": 5} ]

for case in testcases:
    print(s.combinationSum2(case["candidates"], case["target"]))

