# Problem
Given an integer array `nums`, return an array answer such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

Follow up: Can you solve the problem in `O(1)` extra space complexity? (The output array does not count as extra space for space complexity analysis.)
 

### Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

### Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

### Solution
1. can split up to find prefix and suffix product of a number in the array
    - prefix product is all numbers before it multiplied
    - suffix product is all numbers after it multiplied
2. then answer for any number is it's prefix and suffix product multiplied
3. use loop to find prefix product
    - start at beginning (the first number always have product 1 since nothing before it, initial product is 1)
    - then mult the current product by current number (this will be product for the next number)
    - if we have [2,4,6,8], 2 will have 1 since that was initial, but we then mult current product (1) with 2 to get 2, which is the product for the next number
    - when we are calcualting the product of the next number, we doing it as we go so we onlu need to multiply the current product by the current number
4. suffix product follows same logic it just starts at the end of the list instead