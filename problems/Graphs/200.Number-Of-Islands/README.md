# Problem

Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Example 1

```bash
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

### Example 2

```bash
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

### Solution

We can use the idea of connected components of a graph, we can treat 1's that are adjacent as connected and ignore and 0's since they don't make up an island.

So when traversing with BFS:

- We determine the current neighbors as the adjacent positions: `top, right, down, left`
- We only consider positions that are in bounds and also if they are 1's, we ignore 0's
- Keep track of visited set between BFS traversals

We can then iterate over the 2d grid and only call BFS if the tile is a land tile that has not been visited. So every time we do BFS we would be traversing a new island so we can increment a counter every time we BFS which would be our island count.
