# Problem

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```java
class Node {
  public int val;
  public List<Node> neighbors;
}
```

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the copy of the given node as a reference to the cloned graph.

### Example 1

```bash
1 -- 2
|    |
4 -- 3

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

### Solution

Must create deep copy, meaning that we create new nodes with same values and neighbors but we can't use nodes from original graph as that would be using same reference, references must be different because deep copy.

To make sure we don't create duplicate nodes we will use hash map to keep track of our cloned nodes. Key would be `val` of of original node
and the value would be the actual cloned node. We can use `val` of original nodes instead because `val` is unique.

We then perform BFS on original graph and created the cloned graph as we go:

- when moving to new node, create clone if it doesn't exist in hash map: `clonedNode = Node(val=node.val, neighbors=[])`
- when iterating over `node`'s neighbors, we also do same and create clone if it doesn't exist: `clonedNeighborNode = Node(val=neighbor.val, neighbors=[])`
- after creating neighbor if it doesn't exist we add neighbor to `node`'s neighbors'

From BFS we can return the hash map of all the cloned nodes. When returning, problem wants us to return the clone of the given node, so
we can just access the hash map by the given node's `val`: `return nodeMap[node.val]`
