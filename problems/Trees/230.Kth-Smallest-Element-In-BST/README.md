# Problem
Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (1-indexed) of all the values of the nodes in the tree.


### Example 1:
```
  3
 / \
1   4
 \
  2

Input: root = [3,1,4,null,2], k = 1
Output: 1
```

### Example 2:
```
      5
     / \
    3   6
   / \
  2   4
 /
1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```


### Solution
Inorder traversal (left, root, right) is guaranteed to be in increasing order, so we can just add all node values to an array. Because it's going tp be increasing order, the array will be all the nodes in ascending order. Then we can just use `k` to index into the array: `k - 1` because it is 1-indexed.