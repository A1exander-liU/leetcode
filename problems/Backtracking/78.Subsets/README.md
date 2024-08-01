# Problem

Given an integer array `nums` of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

### Example 1

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

### Example 2

```
Input: nums = [0]
Output: [[],[0]]
```

### Solution

The subsets contain at least one element or all elements from `nums` so we need to add a subset at each step of iteration. Since subset can contain up to size of `nums`, we need to iterate size of `nums` times.

For each element the next element that we choose to be part of our subset has to be an element after the current one. We can't use the elements again since the each number cannot be reused. If we already added `1` to our subset to make another subset we cannot choose `1` again and also since we are iterating over `nums` this is another reason why we can choose previous ones since they were already considered.

```
[1] [1,2] [1,2,3]
 1 -> 2  ->   3 ->  end
    [1,3]
  ->  3  -> end

[2]  [2,3]
 2 ->  3  -> end

[3]
 3 -> end
```

For base case, once we reached the end of the `nums` we should return as there would be no numbers after to choose from.
