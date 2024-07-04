# Problem
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”

Constraints:
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the BST.


### Solution
In BST, for each node all nodes to its `left` are smaller or equal to it and all node to its `right` are greater or equal to it. So if you have node `6`, its `left` has to be `<= 6` and its `right` has to be `>= 6`. We can use this to help determine where the lowest common ancestor is.

If both `p` and `q` are smaller than current node that means going `right` would be redundant as all nodes on `right` are greater or equal to current node so if they are both smaller than current node, then no need to check `right`. This means we can just go left.

If both `p` and `q` are greater than current node that means going `left` would be redundant as all nodes on `left` are smaller or equal to current node so if they are both bigger than current node, then no need to check `left`. This means we can just go right.

Now to know if we found the lowest common ancestor, if it does not match the above 2 cases then we found as there is no where left to traverse. Basically
when we find a split like either `p` or `q` is smaller/bigger than current node and then the other is the other way (`p` is `2`, `q` is `4` and `current` is `3`). Also the case when we found common node when `p` or `q` is equal to current node, this means we already found both nodes so searching further down
is meaningless as each node is unique (In example 2, `2` would equal `p` so we stop, otherwise if we keep searching we would lost `2` since each node unique).
