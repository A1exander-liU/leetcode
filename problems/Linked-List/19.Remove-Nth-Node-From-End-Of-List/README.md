# Problem
Given the `head` of a linked list, remove the `nth` node from the end of the list and return its `head`.


### Example 1:
```
1 -> 2 -> 3 -> 4 -> 5
to
1 -> 2 -> 3 ------> 5

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2:
```
1
to
[]
Input: head = [1], n = 1
Output: []
```

### Example 3:
```
1 -> 2
to
1 ->
Input: head = [1,2], n = 1
Output: [1]
```


### Solution
For first example if `n` is 2 that means we remove the second last node. If we look at it like an array, then there are 5 elements and the index of the
node we want to remove is 3. To calculate the index to remove we can do `len(nodes) - n` (eg. 5 - 2 = 3).

But we have a linked list so we don't have indices, so instead we can iterate and add our nodes to an array: `[1, 2, 3, 4, 5]`. Now that we have this we can get the node we want to move like `nodes[remove_index]`. Now all we have to update the links between the nodes.

For updating links, there are 2 different cases: the node we want to remove is the `head` or not. When we want to remove the `head` we have to update with new `head`. If we have `[1,2]` and we remove 1, our `head` has to be updated to 2: `head = head.next`, so we just update `head` to point to the node after current `head`. If we are not removing the `head` we don't need to update it. If we have `[1,2,3,4,5]` and we want to remove 4, we need to update the previous node 3's `next` to point to 5 now instead of 4, that means we have to update it to point the `next` node after the node we want to remove: `prev_node.next = node_to_remove.next`.