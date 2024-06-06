from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(["+", "-", "*", "/"])
        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                match token:
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num1 - num2)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        stack.append(int(num1 / num2))

        return stack[0]
