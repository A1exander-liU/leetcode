# Problem
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.


### Example 1:
```
  root  
    3
   / \      subRoot
  4   5       4
 / \         / \
1   2       1   2

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

### Example 2:
```
   root
    3
   / \        subRoot
  4   5         4
 / \           / \
1   2         1   2
   /
  0

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```


### Solution
So we want to know if `subRoot` is a subtree somewhere in `root`, also if they are both the same it counts as being a subtree as well. We can traverse the tree and keep track of the current order by appending the value of the node we visited to an array. Note that if the node is null we should append `null` to instead. We need the null nodes to make sure the trees have the correct visit order. 
```
  a        b
  1        1
 /          \
2            2

If you don't account the null nodes in the visit order you get:
a = [1,2]
b = [1,2]
But tree a and b don't have same structure

With accounting the null nodes:
a = [1,2,null,null,null]
b = [1,null,2,nul,null]
Now it is correct order
```

In example 1, the orders would be:
`root =    [3,4,1,null,null,2,null,null,5,null,null]`
`subRoot = [4,1,null,null,2,null,null]`
For example 1, the answer is `true` so `subRoot` does exist as a subtree of `root` and we look at the arrays here, `subRoot` visit order exists also as a
subarray of the `root` visit order. With this we can just check if the `subRoot` visit order exists as a sub array of the `root` visit order.