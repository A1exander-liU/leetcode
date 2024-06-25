# Problem
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.
- `int get(int key)` Return the value of the `key` if the `key` exists, otherwise return `-1`.
- `void put(int key, int value)` Update the `value` of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions get and put must each run in `O(1)` average time complexity.


### Example 1
```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```


### Solution
Calling `get` and `put` on a key both count as being used. If `capacity=2` and we have the keys: `[1,2,3]` then after calling `get(1)`, `get(3)`, and `put(2, 4)` we call `put(4, 1)`, we evict key `1` as `3` and `2` was more recently used since the `get(3)` and `put(2,4)`  was called after `get` on `1`. 

If keys are like: `[1,2,3]` and keys are in order of least to most recent, when we do `get(1)`, `1` becomes the most recent as it was just used. It would like: `[2,3,1]` instead, since using it makes it the most recent, it should move to the end. So everytime we use a `key`, we should move it to the end.


To store the information we will use doubly linked list because it's fast to update and delete nodes since you only have to update the pointers, with `[1,2,3]`, we do `get(2)`, we would have to move `2` which would just be updating the `next` and `prev` pointers of the nodes before and after it and adding it to the tail. But if just have a `key` we would just have to search whole linked list to find the node we want, but we can also combine with hashmap so the keys are the keys and the values are the nodes to avoid iterating over linked list to find node we want. Because we using doubly linked list, we should include a `head` and `tail` variable to know when the linked list begins and ends.

Our node will look like this:
```python
class LRUNode:
  def __init__(self, val: int):
    self.prev = -1
    self.next = -1
    self.val = val
```

So when we for `put`:
- If the `key` already exists we will just update its `value` and move the node to end, updating `tail` to be this node
- If `key` is new but there is no room, we will remove the `head` and update `head` to be node after or nothing if there was only 1 node on top of add creating a new nod and adding it to end
- If `key` is new but there is still room we can just create the node and add to the end

For `get`:
- If the `key` doesn't exist we return `-1`
- If it exists, we move the node to the end and return its `value`