# Problem

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of candidates where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

### Example 1

```bash
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

### Example 2

```bash
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

### Example 3

```bash
Input: candidates = [2], target = 1
Output: []
```

### Solution

Because we can reuse the `candidates` an any number of times, we would keep using the current number until our `currentSum > target`. In example 1 we would keep going with `2`:

```bash
[2,3,6,7]
target: 7

2 -> 2 -> 2 -> 2 -> x (currentSum = 8)
            -> 3
```

Every time we add a number we would add this to our `currentNums` array, this way we can track the combinations. When we our `currentSum == target` we can add our `currentNums` to the `result` array.

Once we use 4 `2`s, our `currentSum` is greater than the `target` so we would move to next candidate `3`. Since we are changing choices we should pop from our `currentNums` as the last number means that with addition of it we ended up being over the `target`.

Now to handle duplicate combinations when we choose the next candidate it should never be a candidate before current number.

```bash
[2,3,6,7]
target: 7

2 -> 2 -> 2 -> 2 -> x
       ...
       -> 3 (7)

3 -> 2 -> 2 (7)
```

In example 1 we would end up with duplicate: `[2,2,3]` and `[3,2,2]`, since the second time when the combination starts at `3` uses `2`, it is already going off on a previous combination as we are going over the `candidates` in order.
