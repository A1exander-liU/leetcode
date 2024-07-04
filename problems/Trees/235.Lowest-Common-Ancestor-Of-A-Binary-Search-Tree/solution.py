from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        lowest = [root]

        def lowestCommonAncestorHelper(
            node: "TreeNode", p: "TreeNode", q: "TreeNode", result: List[TreeNode]
        ) -> None:
            if node is None:
                return

            result[0] = node

            if node.val > p.val and node.val > q.val:
                lowestCommonAncestorHelper(node.left, p, q, result)
            elif node.val < p.val and node.val < q.val:
                lowestCommonAncestorHelper(node.right, p, q, result)

        lowestCommonAncestorHelper(root, p, q, lowest)

        return lowest[0]
