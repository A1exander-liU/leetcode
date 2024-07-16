# Problem
Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?


### Example 1:
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

### Example 2:
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```


### Solution
Since we want to find `kth` largest in the array we can use a min heap to store the top `k` elements. If we store the top `k` elements then the `k` largest element would be the smallest of these and since we are using a min heap that means the `k` largest element would end up being our root.

Now we just need to add our values to our heap while:

If our heap is full and next element is bigger than our root:
- We would pop from the heap to remove our root and add the new element
- We would get rid of smallest as we only ever want top `k` elements so if we have `[4,5,8]` and need to consider `9` the smallest would end up on longer being part of the top `k` as the new element is bigger than it.

If our heap is not yet full:
- We can simply just add the new element to our heap

Then at the end, all we need to is return the root `heap[0]`.