# Problem

Given `n` nodes labeled from `0 to n-1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

### Example 1

```bash
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
```

### Example 2

```bash
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
```

### Solution

Tree is a connected graph with no cycles, so we need to make sure its connected and acyclic.

Since we only get `n` and the `edges`, we can build graph from `edges`. We can use dict to map each node to a list of neighbors.

iterate over all edges:

- edge is `node1 -- node2`, since undirected each node has each other as neighbor (for node1: `graph[node1].append(node2)`)

then iterate over `n` to initialize empty lists for all other nodes. Say `n` = 3 and there is one edge: `[0,1]`, the edges may not represent
all the nodes.
while going over the edges, we can do an early return if both values are the same for a given edge: `[1,1]`, this means `1` is connected
to `1` so there is a cycle here.

```bash
0 -- 1    2

edge between 0 and 1 but 2 is by itself
```

To determine if connected can use `visited` set and loop over all nodes:

- only dfs on nodes that aren't visited
- use `count` to track number of dfs, if more than `1` than its not connected

To determine if there is cycle we can use dfs and check if we would revisit a node:

- every time we dfs, we can track the node we will visit and also the parent node (the node it came from)
- if one of node's neighbor is already visited and its not the parent than there is a cycle

we don't include parent as parent will always be a neighbor of current node, as you current node was only reached by traversing from parent, meaning they must be neighbors.
