from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(val=preorder[0])

        node = TreeNode(val=preorder[0])
        inorder_root_index = inorder.index(preorder[0])

        left_end = inorder_root_index

        left_preorder = preorder[1 : left_end + 1]
        left_inorder = inorder[:inorder_root_index]

        right_preorder = preorder[left_end + 1 :]
        right_inorder = inorder[inorder_root_index + 1 :]

        left_node = self.buildTree(left_preorder, left_inorder)
        right_node = self.buildTree(right_preorder, right_inorder)

        node.left = left_node
        node.right = right_node

        return node
