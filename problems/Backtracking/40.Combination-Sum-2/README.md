# Problem

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in candidates where the candidate numbers sum to `target`.

Each number in `candidates` may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

### Example 1

```bash

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

### Example 2

```bash
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
```

### Solution

Since we can't have duplicates we should presort the array first, this makes sure the duplicate candidates are next to each other which
makes it easier to check. We also need to use loop to start from each candidate. Since we are iterating over candidates, when picking next
candidate, only pick ones after (higher index).

```bash
1 ->
2 ->
..
..
```

Consider example 2 when don't sort and try to find the combos that add to `5`.

```bash
[2,5,2,1,2]
2 -> 2,5
  -> 2,2 -> 2,2,1
  -> 2,1 -> 2,1,2

# 2,2,1 and 2,1,2 are the same combos so this is not correct
# if we check for same combo we may have to sort both and check if they equal which is expensive

[1,2,2,2,5]
1 -> 1,2 -> 1,2,2
  -> 1,2 -> 1,2,5

# here because the 2's are next to each other, we can skip if previous was same so we only use the third 2'
```

Thus every time we backtrack we skip candidates that are the same as previous.
