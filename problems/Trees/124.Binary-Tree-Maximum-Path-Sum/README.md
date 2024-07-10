# Problem
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum path sum of any non-empty path.


### Solution
We can do a bottom-up approach and calculate the max path as we go up. Our base case would be when our `node` is null, when this happpens we should also return 0. For example 2, if we look at node 15, it has nothing to its left and right so we return 0 to make sure value would not be changed.

In example 2, if we traversed from 15 and 7 back to node 20, node 20 would get 15 for its left and 7 for its right, now to calculate the max path so far we would have to add these values. We can't just add all 3 together, the current val, and its left and righ together because we don't know their values, they could be large negative numbers so adding all 3 may result in a smaller number. So there are several cases to consider:
- If the current value itself may be largest without adding (what if both left and right negatives)
- the current + left may be largest (right may be negative)
- the current + right may be largest (left may be negative)
- or current + left + right may be largest (both left and right are positive)

So we need to update our current max based on these cases. Now when we return the value up to the node above, we can't just return the max value because it may not be a valid path. Thde node up from 20 is node -10, based on our conditions the max at node 20 would be: `20 + 15 + 7 = 42`, but we can't return 42 up because this value represents the node 20 and both its children:
```
  20
  / \
15   7
```
If we pass 42 up we won't get a valid path anymore:
```
-10
  \
  20
  / \
15   7
```
This is not a path anymore since it branches at node 20, so instead we need to which path is better:
- just current (a node itself is a path, if we adding left or right makes value smaller because they are negative)
- current + left (if left path is better, right is negative or smaller)
- current + right (if right path is better, left is negative or smaller)

So based on these the path we would return back up is left path: `20 + 15 = 35`:
```
-10
  \
  20
  /
15
```
Now we have a valid path.