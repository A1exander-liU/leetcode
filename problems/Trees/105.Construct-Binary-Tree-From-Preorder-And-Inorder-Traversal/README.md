# Problem
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.


Constraints:
- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of unique values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be the preorder traversal of the tree.
- `inorder` is guaranteed to be the inorder traversal of the tree.


### Example 1:
```
  3
 / \
9  20
   / \
  15  7

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

### Example 2:
```
   -1
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```


### Solution
Note how each traversal works, preorder: root, left, right, inorder: left, root, right. This means that in `preorder`, the first element will always be the root of the tree as the root is visited first (preorder: `[1,2,3,5]`, first element is guarnteed to be the root). Since they both contain the same elements `preorder` and `inorder` are the same length.

Now for `inorder`, since its left, root, right, all left elements are visited first then root then all right elements. This means that in `inorder` all elements to left of root val is in left subtree and all to right are in right subtree. For example 1, root is 3 (first element of preorder is root), that means if you look at value 3 in `inorder` : `[9,3,15,20,7]`, left would be `[9]` and right would be `[15,20,7]`, this is same if you look at the binary tree in example 1 which does contain 9 on its left subtree and 15,20,7 on its right subtree.

For example 1 we do example of building tree and tracking the preorder and inorder. preorder and inorder will be shown to right of each node.
```
               3 [3,9,20,15,7] [9,3,15,20,7]
              / \
    9 [9] [9]    20 [20,15,7] [15,20,7]
                    /            \
                 15 [15] [15]    7 [7] [7]



              -1 [-1] [-1]
             /  \
          [] []   [] []

```

By look at this we can some patterns at each level we split into left and right subtree.
- First element in `preorder` at each level is used to divide into left and right subtree
  - For node 20, `preorder` is `[20,15,7]`, so 20 is current root at this level
- `inorder` is split, everything to left of the current root is left subtree and all to right is right subtree
  - For node 20, in `inorder` all to left of 20 is `[15]` and all to right is `[7]`
  - so `inorder` for each left and right subtree would just be a splice of the array based on all elements to left or right
- When `preorder`/`inorder` is length of 1 or 0, we can't divide further so this would be our base cases

For determining which nodes are part of left and right subtree's `preorder` we can use splices of the `inorder`. In example 1, for first level, we know our root is 3 so when we split the `inorder` into left and right we get: `left: [9] right: [15,20,7]`. Note that these arrays also tell us how big the subtrees are, left here is length 1, only 1 node on left subtree. For right length is 3. We can use this length information for splitting the `preorder`. Since the order for preorder is root, left, right, after our root element it will be all the left elements followed by the right elements. Since we know the size of left and right from `preorder` then if our left: `[9]` is length 1 then left in `preorder` is `preorder[1:1 + len(left)]`, we start at 1 since first element is our root. Right would be `[1 + len(left):]`, since right continues off from left it would be like this.

Since we now know how to split them up we can use divide and conquer to build the tree. We can find each node's `left` and `right` and update the current node's `left` and `right` to these nodes, then we reutrn our current node so next level up will use our current node. From the patterns above, when `preorder`/`inorder` is length 1 or 0 we have a base case. When length is 0 we return 0 that means there is nothing to left or right, then when we have length 1 we just create a new node using the value of current root (the first element in `preorder`). 

It would be like this for example 1, looking at nodes 15,20,7
```
   20 [20,15,7] [15,20,7]
      /            \
  15 [15] [15]    7 [7] [7]



When we get to 15 would create a node with value of 15 since length is 1, so node 15 would be returned back to node 20
WHen we get to 7, we would create a node with value of 7 since length is 1, so node 7 would be returned back to node 20

So node would get node 15 for its `left` and node 7 for its `right`

Then it returns itself so it can returned back to the node above it or exit if it was the root.
```
