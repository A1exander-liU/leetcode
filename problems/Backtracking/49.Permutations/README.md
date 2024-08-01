# Problem
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.


### Example 1:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3:
```
Input: nums = [1]
Output: [[1]]
```


### Solution
We can keep track of array `current` to store current numbers of our permutation, will start as `[]`. Since permutation is just a rearrangement, once we added all numbers to `current` (when `current` is same length as `nums`) this will be base case and can add `current` to `result` array.

We want to use one of each number in `nums` so each time we pick a number we should only choose a number we haven't already added to `current`, so we just need to check if the number is in `current` or not.
```
1 -> 1,2 -> 1,2,3
  -> 1,3 -> 1,3,2

2 -> 2,1 -> 2,1,3
  -> 2,3 -> 2,3,1

3 -> 3,1 -> 3,1,2
  -> 3,2 -> 3,2,1
```
