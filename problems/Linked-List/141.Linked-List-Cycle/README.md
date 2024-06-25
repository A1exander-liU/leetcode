# Problem
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

Follow up: Can you solve it using `O(1)` (i.e. constant) memory?


### Example 1:
```
3 -> 2 -> 0 -> -4
     ^__________|

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### Example 2:
```
1 -> 2
^____|

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

### Example 3:
```
1

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```


### Solution
By looking at the examples, if we doing an example iteration we can tell if there is a cycle if a node was iterated over more than once. In example 1, `2`, `0`, and `4` would be constantly iterated over because once you hit `4` you go back to `2` and cycle continues. What we can then do is track all the nodes we iterated over, if we then check if our current node is in the nodes we iterated over that means we iterated over this node more than once; so there is
cycle.

This works but the follow-up wants to use `O(1)` space, meaning we can't just store all the nodes now since that would be `O(n)`. We can use a fast and slow pointer approach, where `slow` moves 1 node at a time and the `fast` moves 2 nodes at a time. While moving if either of them reach the end (current is null), that means there was never a cycle. If there was a cycle, both `slow` and `fast` would constantly loop through the linked list, since the `fast` is moving twice as fast as the `slow` it would pass the `slow` but a certain point it `fast` will catch up to `slow`: they are both on the same node. When this happens we know there is a cycle.
```
example 1 nodes

slow: 3 2 0 4
fast: 2 4 2 4
dist: 1 2 3 0

```
when start, `slow` is at node 3 and `fast` is at node 2 and are 1 node away
after they are at 2 and 4, the distance is 2 which is increasing by 1
then when `slow` is at 0 and `fast` is back at 2, distance is 3
then aterwards distance becomes 0, which is when they meet

notice how distance keeps going up by 1 and stops increasing at 3. 3 is also the number of nodes that are part of the cycle: `[2,0,4]`
so the distance keeps increasing until the length of cycle then the `slow` and `fast` finally meet.