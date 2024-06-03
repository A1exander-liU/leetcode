# Problem
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.


### Example 1:
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Example 2:
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9 
```


### Solution
1. Since we want to find consecutive sequence we can just sort the array in ascending order
2. with sorted array we can check if next number is the previous number + 1, sequence ends when next number is more than prev + 1
   - keep track of how long current sequence and compare against global max
3. to not have to deal with cases of the same number, along with sorting we can also turn it into set to remove dupes