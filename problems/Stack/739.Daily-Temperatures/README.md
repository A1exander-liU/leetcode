# Problem
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.


### Example 1:
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

### Example 2:
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

### Example 3:
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```


### Solution
So we want to find the next greater temperature for each temperature and determine how far apart they are.

1. so how to find how many days each one needs? look at `[73,74,75,71,69,72,76,73]`. we look at the first `73` the next greater temp is `74` and its 1 day difference
   - `73` is at index 0 and `74` was at index 1, (1 - 0 = 1) so we can use the distance between the indices to determine how many days.

2. to find next greater, naive way would be look through all temperatures after current one each time
   - slow since scanning the array every time
3. can use monotonic stack (all items are in specific order: either increasing or decreasing) instead since we want to find next greater element
4. what we do keep adding elements, removing elements that are less than current element to be added
5. in beginning we just add 73's index: 0 
   - now we move on and have 74 to add next but 74 is bigger than `temperatures[0]` which is 73. since its bigger we already find the next warmer temperature for 73
   - when find the next warmer temperature we remove `0` off the stack and calculate the days for it with: `result[top] = i - top`
   - then we add 74 to stack and repeat whole process
   - essentially we are adding the temperatures we want to find next warmer temp and remove them once we find a warmer temperature