# Problem
You are given the `head` of a singly linked-list. The list can be represented as:

`L0 → L1 → … → Ln - 1 → Ln`
Reorder the list to be on the following form:

`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


### Example 1:
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

### Example 2:
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```


### Solution
So basically we need to rearrange all the nodes apart from the `head`. The next nodes that will follow will be the last node and first node after `head`. Then the second last node and the second node after `head`, then third last node and third node after `head` and so on. So in example 1,
the first node `1` remained unchanged, and then we add the last node (4) than the first node after `head` (2) so it is like: `1 -> 4 -> 2`. Then we would add second last node and second node after `head` but since there is only a `3` left, we just add `3`: `1 -> 4 -> 2 -> 3`.

What we can do is add the elements after `head` to a deque (double ended queue) so we get: `[2,3,4]`. We can then do a `pop()` and `popleft()` to get the ends of the deque. Doing `pop()` will give `4` and `popleft()` will give `2`. With this we can update the links:
```python
right = deque.pop()
left = deque.popleft()

current.next = right
right_node.next = left
left.next = None # make sure to unlink from original order to prevent cycle
current = left # since left was the last node added we update current to point it
```

Now we need to also handle the case where there is 1 node in deque, in the example after we relinked to: `1 -> 4 -> 2`, we only had `3` left to link. If we `pop()` and `popleft()` with only one node left, we will get error because the deque would be empty. So when there is only 1 node left, we have to only do it once: `pop()` 
```python
right = deque.pop()

current.next = right
right.next = None
current = right
```
