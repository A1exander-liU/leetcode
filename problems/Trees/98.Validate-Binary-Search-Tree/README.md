# Problem
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.


### Example 1:
```
  1
 / \
2   3

Input: root = [2,1,3]
Output: true
```

### Example 2:
```
  5
 / \ 
1   4
   / \
  3   6

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

### Solution
When doing a inorder traversal (left, root, right) on a BST the node values are guarnteed to be in increasing order.

```
  2
 / \
1   3

Inorder: [1,2,3]
```

So basically we can store the node values in array and compare the current node's `val` against the last element in the array. If the current value is not greater than it is not a valid BST.