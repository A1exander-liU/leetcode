from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalancedHelper(node: Optional[TreeNode], result: List[bool]) -> int:
            if node is None:
                return 0

            left_depth = isBalancedHelper(node.left, result)
            right_depth = isBalancedHelper(node.right, result)

            if abs(left_depth - right_depth) > 1:
                result[0] = False

            return max(left_depth, right_depth) + 1

        if root is None:
            return True

        result = [True]
        isBalancedHelper(root, result)

        return result[0]
