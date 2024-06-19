# Problem
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a *deep copy* of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) that the random pointer points to, or `null` if it does not point to any node.

Your code will only be given the head of the original linked list.


### Example 1:
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

### Example 2:
```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

### Example 3:
```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```
 

### Solution
We are basically making a new linked list with same order as the nodes in the original linked list, means we will be *creating* new nodes like `Node()`.
We also have to make sure the `random` of each node points to the same node they originally pointed to as well, if a node's `radnom` points to the first node we have to make sure it still does that in new list.

With `random`, say you have make copy of node, and the `random` points to itself in orignal list, how would you check that it points to itself so you would use the same node to be `random` rather than making a new node. Basically how can you tell which node the `random` points to so you know if you need to use
an existing node already created or create a new one.

Can use a hashmap to store a mapping between the original node and the new copied node. Say there is original node you would store like: `hashmap[original_node] = Node(val=original_node.val)` then if this orignal node has a `random` that points to itself you can know by just checking the hashmap:
`if original_node.random in hashmap` then we can get back the same node for `random` (when doing key checks with objects, it checks if same address).
Now what if `random` points to something that does exist yet? We can just make it. We can do the same thing for the `next` as well they all point to some node in the linked list. 

So basically what we have is create the node in the hashmap if it does exist. Then we just assign the copied node and its `next and `random` from nodes in the hashmap.
```python
if current not in hashmap:
  hashmap[current] = Node(x=current.val)

  current_copy = hashmap[current]

  if current.next not in hashmap:
      hashmap[current.next] = Node(x=current.next.val)

  if current.random not in hashmap:
      hashmap[current.random] = Node(x=current.random.val)

  current_copy.next = hashmap[current.next]
  current_copy.random = hashmap[current.random]
```