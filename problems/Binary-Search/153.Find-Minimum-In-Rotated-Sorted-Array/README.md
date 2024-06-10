# Problem
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.
- 
Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.


### Example 1:
```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

### Example 2:
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

### Example 3:
```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
```


### Solution
First thing we can do is split the array each time in 2 parts: the sorted portion and the rotated portion.
If you look at `[7,0,1,2,4,5,6]`, we you first do binary search you get `2` as the `mid`. To the left of `mid` we can see that `[7,0,1]` is rotated
portion since it is not in ascending order (the array was sorted in ascending order and was **then rotated**). So we can compare the `mid` and `left`
values to determine if its rotated by doing `nums[mid] > nums[left]`. We want to make sure the `mid` element is greater because if you consider no rotation, the higher index would be a larger number because the array is sorted in ascending order.



Now we have 2 portions: `[7,0,1]` and `[2,4,5,6]`. We will always move to sorted side first. But once in sorted side when should we move left or right. If we just look at we know we should move to the `[7,0,1]` so we would update the `right` variable.
```
[7,0,1,2,4,5,6]
[7,0,1] [2,4,5,6]
```

To figure this out we can compare the last element of each section: `1` and `6` and move to the side that has the smaller last element. We don't compare the first elements cause of rotation, in this case it would be `7` and `2` and we would end up going to the wrong side. Comparing the last elements  works because we know the array is sorted in ascending order. 

So if left side is sorted we can do this to move to left side: `nums[mid] < nums[right]`, meaning the left side contains the smaller value than right side so we move our `right` otherwise `left`. 
,
Now this works if our left side is sorted, we need to do a different check if right side is sorted: `nums[right] < nums[max(0, mid - 1)]`, meaning if the right end is smaller than the left end we contine moving right so update the `left` otherwise update the `right`


Now we should update our `min_val` whenever we find the side with the smaller end. But what to update our `min_val` with? We should use the beginning of the portion since we look at the sorted side and its is sorted in ascending order so the smaller index should have a smaller value. Will update with `nums[left]` or `nums[mid]` because if sorted is left side it would go from `left` to `mid` so `left` is smallest index. But if right is sorted it would
go from `mid` to `right` so `mid` is smallest index.