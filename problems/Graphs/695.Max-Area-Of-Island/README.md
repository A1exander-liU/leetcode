# Problem

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Return the maximum area of an island in `grid`. If there is no island, return `0`.

### Example 1

```bash
0 0 1 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 0 0 0
0 1 1 0 1 0 0 0 0 0 0 0 0
0 1 0 0 1 1 0 0 1 0 1 0 0
0 1 0 0 1 1 0 0 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0 0

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

### Example 2

```bash
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

### Solution

Traverse whole entire grid and perform BFS when we reach a land tile, will use a `visited` set to make sure we don't BFS on land tiles
we already visited from a previous BFS.
In BFS we traverse all neighbors (top, right, left, down) that are:

- not out of bounds
- not a water tile
- not yet visited

This means we will end up visiting all connected land tiles starting from land tile we used. We will use a counter and increment every time
we traverse to new node to find area of this island.

Compare current max each time against area of new island.
