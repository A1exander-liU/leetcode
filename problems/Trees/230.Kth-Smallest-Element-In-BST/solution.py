from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kthSmallestHelper(root: Optional[TreeNode], result: List[int]) -> None:
            if root is None:
                return

            kthSmallestHelper(root.left, result)
            result.append(root.val)
            kthSmallestHelper(root.right, result)

        result = []
        kthSmallestHelper(root, result)

        return result[k - 1]
