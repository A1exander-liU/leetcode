# Problem
You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

If `x == y`, both stones are destroyed, and
If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return `0`.


### Example 1:
```
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
```

### Example 2:
```
Input: stones = [1]
Output: 1
```


### Solution
In the game we always want to get the next 2 largest stones with the largest weights, meaning that we can utilize a max heap for this problem. We would start by adding all the weights into a heap.

Now since we have to keep getting the next 2 largest stones, we should only keep going if the size of our heap is greater than 1. Now we would just pop from the heap twice, first time for `y` (`x <= y`, meaning `y` is the larger value so it should store first popped value from heap) and second time for `x`.

Now we just need to compare, we don't need bother comparing `x == y` as since we already removed both stones from the heap there would be nothing for us to do if `x == y`. We just need to handle `x != y` by adding a new weight to our heap that is the difference of `y` and `x`.