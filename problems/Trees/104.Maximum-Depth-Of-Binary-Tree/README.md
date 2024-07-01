# Problem
Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



### Example 1:
```
  3
 / \
9  20
   /\
 15  7

Input: root = [3,9,20,null,null,15,7]
Output: 3
```

### Example 2:
```
   1
    \
     2

Input: root = [1,null,2]
Output: 2
```


### Solution
As we are traversing the tree we can keep track of current depth, since depth is number of nodes along a path we should start with 1 for root node.
Now when traversing down the root node to its `left` or `right` we should increment the current depth by 1 as we are moving down the tree. Since we
are updating the current depth as we are traversing, we should also update the max depth value at each step too.