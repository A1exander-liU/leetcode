# Problem

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1 to n`, with one additional edge added. The added edge has two different vertices chosen from `1 to n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.

### Example 1

```bash
1 -- 2
|  /
3

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

### Example 2

```bash
2 -- 1 -- 5
|    |
3 -- 4

[[1,2], [1,3], [3,4], [3,5], [4,6], [5,6]]
2,1,3,4

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

### Solution

Since tree starts with no cycles, the extra edge added would introduce a cycle. So we basically want to find where the cycle and return last
edge that makes up the cycle.

Use disjointed subsets, each subset will represent connected parts and will initially start as each node being their own subset (`{1} {2} {3}`).

We then iterate over all the `edges`:

- union the 2 sets that contains `ai` and `bi`
  - if at start and we add edge `[1,2]`, `{1} {2} becomes {1,2}`
  - since we added edge between `1` and `2` they are now connected so they should belong to same subset
- if adding edge and `ai` and `bi` are in same set, adding this edge would introduce a cycle
  - adding the edge that connects 2 existing nodes would result in cycle
  - we can then return this edge as our answer
