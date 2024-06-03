# Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Example 1:
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

### Example 2:
```
Input: nums = [1], k = 1
Output: [1]
```

### Solution
1. Create dictionary to track the counts of each number
    - key is the number and its value is it's count

2. Utilize heap data structure (has function that removes biggest/smallest from the heap)
     - idea is we add items in some way so when we pop it using heap it will return the next number with the biggest count

3. Add the key value pairs of `number: count` to the heap
    - can add it in as a tuple like: `(-count, number)`
    - when adding as tuple heap will look at the first element of tuple (smaller will be returned first)
    - negate the count to force the heap to return the largest count instead of smallest count (python heap only does min value not max)

4. Just pop and add to a `result` array `k` times