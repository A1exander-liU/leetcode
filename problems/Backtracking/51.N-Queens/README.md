# Problem

The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

### Example 1

```bash
. Q . .        . . Q .
. . . Q        Q . . .
Q . . .        . . . Q
. . Q .        . Q . .

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

### Example 2

```bash
Q

Input: n = 1
Output: [["Q"]]
```

### Solution

We need to all valid positions can occupy at each step, so before placing queen we need to find new valid positions based on the queens already placed on the board.

Determine where a queen can be placed on each row, check per row because 2 queens in same row can attack
each other (note can also find where a queen can placed for each col):

- use 2d array to represent board to make it easier to update each tile (convert back to array of strings when adding solution)
- use `row` to keep track of current row we want to place next queen
- generate all valid positions in current row
- add current board as solution when `n` amount of queens placed, return to look for other solutions
- return if we run out of valid positions to try different placement

To find valid positions, keep track of queen positions and use set for cols and diagonals to check each col
value on current row.

- iterate over queen positions and create set for both cols and diagonals
- extract col from each position, `pos[1]`
- find current left and right diagonal in row by using difference between the rows: `current row - queen row`
