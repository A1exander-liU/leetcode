# Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example 1

```bash
[A] [B] [C] E
 S   F  [C] S
 A  [D] [E] E

Letters of solution are in []
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

### Example 2

```bash
 A   B   C   E
 S   F   C  [S]
 A   D  [E] [E]

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

### Example 3

```bash
 A   B   C   E
 S   F   C   S
 A   D   E   E


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

### Solution

Backtrack at all tiles that begin with starting letter in `word`. Use `wordIndex` to track which letter we need to find next, increment every time we find current letter.

When backtracking:

- keep track what we visited temporarily mark as ".", restore when we come back
- find valid positions (adjacent and tile must be letter we want to find and not visited)
- go back if we have no valid positions and didn't find whole word yet
- return immediately once we find the word (`wordIndex == word length`), don't backtrack any further

We keep track of visited to prevent using already used tile in current "chain". In example 3, if we try to find "ABCB". Once we hit "C", we find that "B" is a neighbor and that would complete the word but we already
used that "B"

Optimizations:

- Since we just want to know if it exists we should return `true` right away if we find it otherwise we will waste time backtracking all possible starting points
- We can also immediately return `false` if is more than total tiles on the grid, otherwise we may backtrack on a grid with no solution possible.
- Can also use frequency map for the `word` and if starting letter occurs more than ending letter we can reverse the string, this way we would reduce the number of backtracking
