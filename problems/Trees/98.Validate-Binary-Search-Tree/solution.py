from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(
            root: Optional[TreeNode], visit: List[int], result: List[bool]
        ) -> None:
            if root is None:
                return

            isValidBSTHelper(root.left, visit, result)

            if visit and root.val <= visit[-1]:
                result[0] = False
            visit.append(root.val)

            isValidBSTHelper(root.right, visit, result)

        result = [True]
        isValidBSTHelper(root, [], result)

        return result[0]
