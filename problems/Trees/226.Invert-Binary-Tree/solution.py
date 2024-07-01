from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        current = root

        while True:
            if current:
                stack.append(current)

                temp_left = current.left
                current.left = current.right
                current.right = temp_left

                current = current.left

            elif stack:
                current = stack.pop()

                current = current.right
            else:
                break

        return root
