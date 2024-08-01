# Problem

You are given a `m × n` 2D `grid` initialized with these three possible values:

1. `-1` - A water cell that can not be traversed.
2. `0` - A treasure chest.
3. `INF` - A land cell that can be traversed. We use the integer `2^31 - 1 = 2147483647` to represent `INF`.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain `INF`.

Assume the grid can only be traversed up, down, left, or right.

### Example 1

```bash
INF -1   0  INF
INF INF INF -1
INF -1  INF -1
 0  -1  INF INF

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
```

### Example 2

```bash
 0  -1
INF INF

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
```

### Solution

Idea is to traverse using BFS on each land tile until we hit nearest treasure tile marking the land tile with distance once treasure is reached.

We use BFS over DFS because BFS takes one step each time for each direction, so that once we hit a treasure tile we know we already found
the shortest distance to it and can return immediately. DFS will traverse whole entire path until we reach treasure so we would end up
having to traverse every path and compare the minimum distance between all paths. So since BFS allows us to return early it will speed up
the algorithm
Idea is to traverse using BFS on each land tile until we hit nearest treasure tile marking the land tile with distance once treasure is reached.

We use BFS over DFS because BFS takes one step each time for each direction, so that once we hit a treasure tile we know we already found
the shortest distance to it and can return immediately. DFS will traverse whole entire path until we reach treasure so we would end up
having to traverse every path and compare the minimum distance between all paths. So since BFS allows us to return early it will speed up
the algorithm.

To keep track of positions, we will store extra in our queue: `(row, col, distance)`, so we keep track of the position and now also the distance from the start.

When traversing neighbors (top, right, left, down) ignore:

- water tiles since they can't be traversed
- out of bound tiles
- if we already visited this neighbor

When adding our neighbor to queue we do: `q.append((row, col, distance + 1))`. We update the distance by `1` from our current node as going to next neighbor means going one step further.

When current node is a treasure tile we can update the grid and return immediately:

- `grid[start row][start col] = node distance` to update distance of starting land tile
