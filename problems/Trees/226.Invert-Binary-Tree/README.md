# Problem
Given the `root` of a binary tree, invert the tree, and return its `root`.


### Example 1:
```
Original
   4
 2   7
1 3 6 9 

Inverted
   4
 7   2
9 6 3 1

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

### Example 2:
```
Original
 2
1 3

Inverted
 2
3 1

Input: root = [2,1,3]
Output: [2,3,1]
```

### Example 3:
```
Input: root = []
Output: []
```


### Solution
For example 1, when starting from root node we can see that the `left` and `right` subtree was swapped (`2` and `7` to `7` and `2`). If we then look at subtree for `2` and `7` we can see that the nodes are swapped as well. Basically we just need to swap the `left` and `right` of each node in the tree.