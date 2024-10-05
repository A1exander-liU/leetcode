# Problem

There is an undirected graph with `n` nodes. There is also an `edges` array, where `edges[i] = [a, b]` means that there is an edge between node `a` and node `b` in the graph.

The nodes are numbered from `0 to n - 1`.

Return the total number of connected components in that graph.

### Example 1

```bash
0 -- 1
|
2

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1

All nodes are connected so only 1 component
```

### Example 2

```bash
0 -- 1 -- 2 -- 3

4 -- 5

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2

0,1,2,3 are connected and 4,5 are connected so 2
```

### Solution

To determine number of connected components we can loop over all the nodes of the graph and dfs on nodes that have not been visited. Each
time we dfs we would visit all nodes connected to it as only neighbors are visited (if there is edge between them). The number of components
will be the number of times we dfs.

We can build graph from the `edges` mapping each node to a list of their neighbors:

- iterate over all `edges`
- add each other's node to their neighbors `graph[node1].append(node2)` and `graph[node2].append(node1)`
- iterate over `n` to initialize empty neighbors for nodes that aren't connected to others

Then we can dfs over the graph
