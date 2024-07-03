from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], visit_order: List[int | None]) -> None:
            if node is None:
                visit_order.append(None)
                return

            visit_order.append(node.val)

            dfs(node.left, visit_order)
            dfs(node.right, visit_order)

        def isSubArray(arr: List[int | None], subarr: List[int | None]) -> bool:
            n = len(subarr)

            for i in range((len(arr) - n + 1)):
                if arr[i : i + n] == subarr:
                    return True

            return False

        tree = []
        subtree = []
        dfs(root, tree)
        dfs(subRoot, subtree)

        return isSubArray(tree, subtree)
