# Problem
There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.


### Example 1:
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

### Example 3:
```
Input: nums = [1], target = 0
Output: -1
```


### Solution
What we can do first is split our array in 2 portions: the sorted portion and the rotated portion. With `[4,5,6,7,0,1,2]` we have:
`[4,5,6,7]` as sorted and `[0,1,2]` as rotated. To determine which side is rotated we can compare the `left` and `mid` values. If our `nums[mid] > nums[left]` than left side is sorted (since it is in ascending order, higher index should have bigger value than smaller index).


Now to determine how we move, we always want to move to the sorted side since we want to check if `target` is in `nums`. To know if `target` is in a certain side we can check if `target` is inside the boundries of the left or right sorted side:
`nums[left] <= target <= nums[mid]` for left or `mid + 1 < len(nums) and nums[mid + 1] <= target <= nums[right]` for right. This comparision only works if we check the sorted side since the sorted is garunteed to have the lower end value be smaller than the higher end value. In above example, `[4,5,6,7]` was the sorted side because the `mid` value `7` was greater than `left` value 4, we have valid range here since  4 < 7 so we can check if `target` is inside it.

Now when we searching in sorted side, if our `target` is actually not there, we have to move to the other side (the rotated side). Otherwise we will continue searching on same side. So if we move to left as sorted side and couldn't find `2`, we have to move right (so update `left`), if `2` was actually in this range though we would continue searching here by updating `right`. 