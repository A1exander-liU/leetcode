# Problem
You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.



### Example 1:
```
| 1  | 3  | 5  | 7  |
|----|----|----|----|
| 10 | 11 | 16 | 20 |
| 23 | 30 | 34 | 60 |

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

### Example 2:
```
| 1  | 3  | 5  | 7  |
|----|----|----|----|
| 10 | 11 | 16 | 20 |
| 23 | 30 | 34 | 60 |

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```


### Solution
Can treat it like a normal binary search if you view the 2d array (matrix) as 1d. If you have 3 x 4 you can have indices from 0 to 11 (3 x 4 = 12 elements)

Ok so if you look at like 1d you can have 0 to 11, but how to know which maps to actual location in 2d array (matrix)?

Say you do indices from left to right and top to bottom. In the examples if you have index 8, you have the element: 23.
23 is `matrix[2][1]`

So we need to figure out how to turn index 8 into `matrix[2][1]`, basically how to find which row and which column it maps to.
- to determine row we divide by length of a row: `row = index // len(matrix[0])`
  - we divide by length of column because this determines how many fit on a single row
  - if 4 fit on a row you have indices: 0 - 3, 4 - 7, 8 - 11, ...
  - `8 // 4 = 2`
- to determine the column we do modulus instead: `col = index % len(matrix[0])`
  - the remainder basically becomes the offset or position in row (the column)
  - we do it aganst row length again because we want to find which column inside each row
  - `8 % 2 = 0`