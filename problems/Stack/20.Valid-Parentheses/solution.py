class Solution:
    def isValid(self, s: str) -> bool:
        current = []
        brackets = {")": "(", "]": "[", "}": "{"}

        for char in s:
            current.append(char)

            if len(current) < 2:
                continue

            if char in brackets and brackets[char] == current[-2]:
                current.pop()
                current.pop()
            elif char in brackets and brackets[char] != current[-2]:
                return False

        return len(current) == 0
