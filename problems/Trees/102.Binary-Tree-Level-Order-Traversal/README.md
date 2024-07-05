# Problem
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


### Example 1:
```
  3
 / \
9  20
   / \
  15  7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

### Example 2:
```
  1

Input: root = [1]
Output: [[1]]
```

### Example 3:
```
Input: root = []
Output: []
```


### Solution
Since you want to do level by level, you are basically doing a breadth-first search (BFS) but on tree. You are visiting all adjacent nodes (in this case the `left` and `right`) before moving down. 

You can use deque (double ended queue) to keep track of the nodes at each level. When you start you will have deque with just `root` and keep going until
the deque is empty (first level is `root` so just 1 node). Because the deque tracks how many at each level if you iterate and remove the number of items
in queue you have all nodes at current level (start with only deque of size 1 so only need to iterate once).

Before we iterate we can add an empty list to the result first which will be used to store all node values of current level. While iterating we will add our
`node.val` to the `result[-1]` (we just added empty array at before iterating so last index is the one we should add to). While we are adding to `result`
we need to update our deque to contain the nodes for the next level for next iteration, basically we will just add `node`'s `left` and `right` only if they
exist (not null). Make sure to add to `left` first since the problem wants left to right.  