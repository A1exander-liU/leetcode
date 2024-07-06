from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def rightSideViewHelper(
            root: Optional[TreeNode], result: List[int], depth: int
        ) -> None:
            if root is None:
                return

            if len(result) <= depth:
                result.append(root.val)

            rightSideViewHelper(root.right, result, depth + 1)
            rightSideViewHelper(root.left, result, depth + 1)

        result = []
        rightSideViewHelper(root, result, 0)

        return result
