from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], visit_order: List[int | None]) -> None:
            if root is None:
                visit_order.append(None)
                return

            visit_order.append(root.val)

            dfs(root.left, visit_order)
            dfs(root.right, visit_order)

        tree_p = []
        tree_q = []
        dfs(p, tree_p)
        dfs(q, tree_q)

        return tree_p == tree_q
