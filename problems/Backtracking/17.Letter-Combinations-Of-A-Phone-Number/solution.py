from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        numDigits = len(digits)

        def letterCombinationsHelper(
            numIndex: int, combo: str, result: List[str]
        ) -> None:
            if len(combo) == numDigits:
                result.append(combo)
                return

            for letter in phoneMap[digits[numIndex]]:
                letterCombinationsHelper(numIndex + 1, combo + letter, result)

        result = []
        letterCombinationsHelper(0, "", result)

        return result
