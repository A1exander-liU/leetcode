# Problem
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.


### Example 1:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

### Example 2:
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```


### Solution
Note that both arrays are already sorted, meaning you can just merge both arrays together. Essentially you are doing the final step in the merge sort 
algorithm. 

You keep 2 variables to track the index as you are iterating through the arrays `nums1` and `nums2`. At each step you take the smaller of the 2 values
from the 2 arrays and add to a `result` array. When you add the smaller element you increment the index for the array of the smaller value so you can check the next value. This continues until one array runs out of values (all values of the array were added to `result` array) since there is nothing left to compare. Since there is nothing left to compare, you simply add the remaining elements of the other array if any.

After merging the arrays it is easy to get the median by getting the middle value (for odd length) or average of the middle 2 values (for even length).