# Problem

Given an integer array `nums` that may contain duplicates, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

### Example 1:

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

### Example 2:

```
Input: nums = [0]
Output: [[],[0]]
```

### Solution

Keep track of `current` array for storing the subset, since we want to use all the numbers in `nums`, we need to iterate over them at each step and `current` to `result` at each step. To avoid duplicate values we will only add the next number in `nums`, so we will stop once there is no next number (once we reach the final element in `nums`).

We also need to sort the `nums` before to prevent duplicate sets from happening. If `nums=[4,4,4,1,4]`, if we make subsets we would end up with subsets like: `[4,1]` and `[1,4]`, but if we sort we will not get the `1` again because every time we choose the next number after: `nums=[1,4,4,4,4] can get [1,4] but not [4,1]`.
