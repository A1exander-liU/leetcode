# Problem

There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.

### Solution

Problem basically saying find all positions that have a path (where the next cell in path must be less than equal to parent cell) to top or left of the grid (the Pacific) and to the right or bottom of the grid (the Atlantic). We then want to return list of all the positions as list of 2 elements: `[row, col]`

Since top and left of grid is Pacific, if a cell in the path has row of 0 or col of 0 then it reaches Pacific. If look at like 2d array the top and left are basically the first row and first column.

Same idea applies to Atlantic, but instead it would be the last row or last column instead that we need to check the cell for.

Brute Force would be to to BFS at each cell to determine if it reaches both sides:

- neighbors should adjacent and also have `height <= current cell height`
- keep track of 2 flags to check if Pacific and Atlantic are reached
- set to `true` once current cell in path is at first row/col (Pacific) or last row/col (Atlantic)

Instead can do opposite: we can check from the edges rather than each cell since we know edges are always either be able to flow into Pacific
or Atlantic. Perform 2 BFS instead: find all cells that can flow to Pacific and find all cells that can flow in to Atlantic. Since we start from a known valid cell, when checking adjacent neighbors only consider if `neighbor height >= current height` as neighbor needs to flow into the current cell:

- start with all edge cells in queue for Pacific/Atlantic
- use set to store all positions that can flow into Pacific/Atlantic
- BFS and consider only adjacent neighbors that aren't lower than current cell
- add the considered neighbors to the set
- if a position exists in both sets (can flow into Pacific set and can flow into Atlantic set) then it's one of the solution positions
