# Problem

You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`, capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.
- Region: To form a region connect every `'O'` cell.
- Surround: The region is surrounded with `'X'` cells if you can connect the region with `'X'` cells and none of the region cells are on the edge of the board.

A surrounded region is captured by replacing all `'O'`s with `'X'`s in the input matrix `board`.

### Solution

We can BFS all edge regions so we visit them all, then we can BFS over all other regions and update the cell values with `"X"` without needing to check if current region is an edge region.

Check all edge regions:

- first will use shared `visited` set which will be passed into each BFS call
- loop over whole board
- only BFS if position is on the edge (first row, first col, last row, last col) and value is a `"O"` and position not visited
- in BFS visit all connected `"O"`'s (adjacent neighbors that are `"O"` as well)

Check all other regions:

- loop over all cells, start with row 1 and col 1 as we don't need to consider edges
- BFS at `"O"` that are not visited yet
- in BFS visit all connected `"O"`'s, now update cell value with `"X"`
