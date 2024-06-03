# Problem
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

### Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```

### Example 2:
```
Input: nums = [1,2,3,4]
Output: false
```

### Example 3:
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

### Solution
1. can use a set to know if we have duplicate (sets cant have same value)
2. we just loop over the input array and add the numbers to the set
3. also check if we added the number before (if we added the number before that means there is duplicate)
    - checking if something existing in set is as fast as a dictionary