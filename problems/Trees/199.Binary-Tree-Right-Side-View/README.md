# Problem
Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


### Example 1:
```
  1   <-
 / \
2   3   <-
 \   \
  5   4   <- 

Basically you start from right at each level and keeping moving left until you hit a node

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

### Example 2:
```
  1   <-
   \
    3   <-

Input: root = [1,null,3]
Output: [1,3]
```

### Example 3:
```
Input: root = []
Output: []
```


### Example 4:
```
    1   <-
   / \
  2   3   <-
 /
4   <-

Note that it wasn't always the right nodes in the tree, it just keeps going until it hits first node at each level

Input: root = [1,2,3,4]
Output: [1,3,4]
```


### Solution
Basically we want to find the first nodes at each level that we would hit if we start from right side of tree and move left. 

Since we start from the right side of the tree, we will always see a `right` node first if it exists, this means when we traverse the tree we should
traverse the `right` first and then the `left`. 

Because we only want the first node we hit at each level, that means we should only add one node to our `result` array once per level. Basically we can
just keep a parameter `depth` to track at what level the current node we are one. This way we can make sure we only add one node per level by checking
if we already added a node with: `if len(result) <= depth: result.append(node.val)`. We will only add the node if number of nodes we added is less than or equal to depth. We basically use the depth as an index to array `[0, 1, 2]`, if we are at depth 1 and there are 2 nodes added: `[0, 1]`, we would not add another node since we already added one.

