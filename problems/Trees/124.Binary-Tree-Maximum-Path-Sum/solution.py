from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathSumHelper(root: Optional[TreeNode], result: List[int]) -> int:
            if root is None:
                return 0

            left_val = maxPathSumHelper(root.left, result)
            right_val = maxPathSumHelper(root.right, result)

            left_sum = left_val + root.val
            both_sum = left_val + root.val + right_val
            right_sum = root.val + right_val

            best_path_sum = max(left_sum, right_sum, root.val)

            result[0] = max([result[0], root.val, best_path_sum, both_sum])

            return best_path_sum

        result = [root.val]
        maxPathSumHelper(root, result)

        return result[0]
