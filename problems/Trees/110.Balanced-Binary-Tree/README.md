# Problem
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


### Solution
Basically we need to check max depths of each node's subtrees and if at any point if the depths differ by more than one. But this would be very slow
as we would have to traverse the tree multiple times since we have to check each node's subtrees. So instead of traversing each time, we can do bottom-up approach by starting at leaf nodes and calculating deph as we go back up. 

Using example 1, if we start at `4` and check the depths of its subtrees, since it has no children depth is `0` (base case is to return `0` when node is null). Now that we have the depths of its subtrees we have to compare them: `abs(left_depth - right_depth) > 1` and update a variable to set to `false` if it differs by more than `1`. 

Now moving up from `4` and back to `3` we have to update current depth which should be `max(left_depth, right_depth) + 1`, we need max since we need to find
max depths of the node's subtrees and the `+ 1` is to account for the node we are moving back up to. Because we move up 1 node the depth would increase by 1
because of its children nodes. Then we just continue this back up to the top.
.