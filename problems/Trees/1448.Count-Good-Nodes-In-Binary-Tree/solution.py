from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesHelper(root: TreeNode, maxValue: int, result: List[int]) -> None:
            if root is None:
                return

            if root.val >= maxValue:
                maxValue = root.val
                result[0] += 1

            goodNodesHelper(root.left, maxValue, result)
            goodNodesHelper(root.right, maxValue, result)

        if root is None:
            return 0

        result = [0]
        goodNodesHelper(root, root.val, result)

        return result[0]
