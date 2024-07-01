from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [(root, 1)]
        current = root

        max_depth = 1

        while stack:
            current, current_depth = stack.pop()

            max_depth = max(max_depth, current_depth)

            if current.right:
                stack.append((current.right, current_depth + 1))
            if current.left:
                stack.append((current.left, current_depth + 1))

        return max_depth
