# Problem
Given the `head` of a singly linked list, reverse the list, and return the reversed list.


### Example 1:
```
1 -> 2 -> 3 -> 4 -> 5
to
5 -> 4 -> 3 -> 2 -> 1

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

### Example 2:
```
1 -> 2
to
2 -> 1

Input: head = [1,2]
Output: [2,1]
```

### Example 3:
```
Input: head = []
Output: []
```


### Solution
It is only a singly linked list, so you can't start from tail and iterate backwards using prev. How can you iterate it linked list normally while reversing it?

Since we are reversing the order, then each node's `next` should be its previous node. If we keep track of the previous node each time we can then
reverse the list by updating the `next` to be the `prev` node.
```
regular order
1 -> 2 -> 3
reversed order
1 <- 2 <- 3
```

```python
current = head
prev = None
while current is not None:
  current.next = prev
  prev = current
  # updating the next node?
  current = current.next # ?
```

ok so we can update the `next` to be `prev` instead. but we just do this we can't get the `next` anymore since we updated it with the `prev`.
so if we start at first node `1` then it has no `prev` so we update `next` to be `null`. but we want to iterate and update each node's `next`, after updating `1` we want to move to `2` and update its `next` to be `1` now instead of `3`.

so we want to still keep the `next` intact, we can do this by keeping keep a temporary `next` so we can safely update our `next`.
```python
next = current.next
current.next = prev # since next was stored we can now update it with prev node
prev = current
current.next = next # now use the temp next so we can update the next node's prev
```

at the end we then return `prev`, note that the while loop runs until `current` is `null`. this means we passed the last node so `prev` would point to the last node. If we have `1 -> 2 -> 3 -> 4 -> 5`, at the end, `current` would be `null` and `prev` would be `5`.

