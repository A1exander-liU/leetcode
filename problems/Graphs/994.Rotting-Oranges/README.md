# Problem

You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

### Example 1

```bash
R O O   R R O   R R R   R R R   R R R
O O .   R O .   R R .   R R .   R R .
. O O   . O O   . O O   . R O   . R R

  0       1       2       3       4

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
```

### Example 2

```bash
R O O   R R O   R R R   R R R   R R R
. O O   . O O   . R O   . R R   . R R
O . O   O . O   O . O   O . O   O . R

  0       1       2       3       4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

### Example 3

```bash
. R

  0

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

### Solution

Any tile could be a rotten orange meaning that there could be multiple rotten oranges, so first get all initial rotten oranges into queue.
Will have to iterate over the grid, also count number of fresh oranges for checking later after rotting.

Once we have initial rotting oranges:

- do BFS on the initial rotting oranges (BFS because we can only move one step per minute and at each step we can rot all adjacent)
- will use "multi" BFS instead of traverse single at time since ALL rotting oranges each minute can rot adjacent
  - iterate over length of queue, not `while len(queue) > 0` because neighbors will be added to queue as well
- only visit the fresh oranges that have no been visited, mark the grid location with `2`
  - increment `orangesRotted`
- each iteration of BFS we also increment `minutes`
- stop BFS once `orangesRotted == frestCount` (all rotted) or queue is empty (ran out and couldn't rot all)
- at the end, if `orangesRotted == frestCount` then we return `minutes`, otherwise `-1`
