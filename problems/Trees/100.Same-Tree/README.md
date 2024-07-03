# Problem
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


### Example 1:
```
p
  1
 / \
2   3

q
  1
 / \
2   3

Input: p = [1,2,3], q = [1,2,3]
Output: true
```

### Example 2:
```
p
  1
 /
2

q
  1
   \
    2

Input: p = [1,2], q = [1,null,2]
Output: false
```

#### Example 3:
```
p
  1
 / \
2   1

q
  1
 / \
1   2

Input: p = [1,2,1], q = [1,1,2]
Output: false
```


### Solution
If we want to determine if they have same order/structure of nodes and values we can keep track of extra data while traversing. While traversing, can use
an array to store all the node's value we traversed/visited so far. Considering example 1, if we are using DFS and we go down the left first we would get 
`p = [1,2,3]` and `q = [1,2,3]`. We then compare the arrays to check to determine if they are the same trees, since both arrays here have same values and number of elements they are the same tree.

When adding nodes to our array, we also have to add to null nodes as well to maintain order/structure of the nodes. For example 2 if we only add non null nodes, we get `p = [1,2]` and `q = [1,2]`, but they are different trees, so we need the null nodes to account for non existing child nodes. When accounting
for them we get `p = [1,2,None]` and `q = [1, None, 2]`, now we can see they are not the same tree which is correct.