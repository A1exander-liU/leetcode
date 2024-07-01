from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        path connect from a "root" node, this node does can occur at any point of the tree
        finding depth of left and right subtree at each node is too expensive (or is it)

        going botom up instead of top down (with top down, you have to search down longest path for each node's left and right subtree)
        - top down has more repetivive work because u are constantly going to find the bottom nodes
        - if u go bottom up, you dont have to find bttom node each time
        """

        def diameterOfBinaryTreeHelper(
            node: Optional[TreeNode], current_max_diameter: List[int]
        ) -> int:
            if node is None:
                return 0

            left_diameter = diameterOfBinaryTreeHelper(node.left, current_max_diameter)
            right_diameter = diameterOfBinaryTreeHelper(
                node.right, current_max_diameter
            )

            current_max_diameter[0] = max(
                current_max_diameter[0], left_diameter + right_diameter
            )

            return max(left_diameter, right_diameter) + 1

        max_diameter = [0]
        diameterOfBinaryTreeHelper(root, max_diameter)

        return max_diameter[0]
