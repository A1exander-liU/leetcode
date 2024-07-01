# Problem
Given the `roo`t of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The length of a path between two nodes is represented by the number of edges between them.


### Example 1:
```
    1
   / \
  2   3
 /
4

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

### Example 2:
```
  1
 /
2

Input: root = [1,2]
Output: 1
```


### Solution
In example 1, start from `root`, the longest path is `[4,2,1,3]` or `[5,2,1,3]`, since we are currently at root node the longest should be the longest
side of its `left` subtree and the longest path of its `right` subtree (left: `[4,2]`, right: `[3]`) so total would be `3` here. Because the current node,
the `root` connects its `left and `right` you can go from any node from its `left` subtree to its `right` subtree that is why the longest path is combination of both `left` and `right`.

But problem description says that longest path may not between the `root` node, meaning that we have to check each node and determine the max depth for its
`left` and `right` subtree. But finding max depth of each node's subtree is very slow since you have to repeatedly traverse the tree.

But if you start from bottom-up instead where you find depths at the lowest parts of tree and move up it is faster. THen in example 1 if you start at the
lowest (the leaf nodes), what is max path of `4`? Well it has no left and right so answer would be 0, this is our base case here when the node is null, 
we return back 0. Because we keeping track of max, we should update max at each step, since here we found that `left` and `right` is 0 we should compare `0+ 0` against current max (combine depths of both subtrees). Now when we move back up the tree (after we deal with `left` and `right`) we need to pass the updated current diameter. The new diameter should be the max of `left` and `right` diameter added by `1`. We take max of `left` and `right` since we want
to find the longest path so we should always pick the biggest diameter. We add `1` to account for this node to be part of path as we move up, since we are at `4`, the max of its `left` and `right` is 0 since is has no children so if we add `1` we get total of `1` to be returned back to node `2`. So our current path would be `[4,2]`, the `+ 1` is for having `2` as another node on the path.