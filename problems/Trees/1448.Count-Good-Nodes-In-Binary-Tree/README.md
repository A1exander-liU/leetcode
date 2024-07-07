# Problem
Given a binary tree `root`, a node X in the tree is named good if in the path from `root` to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


### Example 1:
```
    [3]
    / \
   1  [4]
  /   / \
[3]  1  [5]

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes surround by [] are good nodes.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```

### Example 2:
```
    [3]
    /
  [3] 
  / \
[4]  2

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```

### Example 3:
```
    [1]
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
```


### Solution
Since we need to know if a node previously on the path was greater, for each path we can keep track of the `maxValue`. So whenever we are at the node we can compare against `maxValue` to determine if its a good node: `if root.val >= maxValue: its good node`. 

Instead of doing 2 separate constant time operations: first find new max and then check good node you can do it in one. 
```python
if root.val >= maxValue:
  maxValue = root.val
  result[0] += 1 # for updating the number of good nodes
```
You can do this because if you update the `maxValue` and it as bigger like `maxValue` was previously `3` but current node `val` is `4` it would still be ok
because current node would be same as `maxValue`.