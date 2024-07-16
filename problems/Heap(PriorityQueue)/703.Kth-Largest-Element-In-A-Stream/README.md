# Problem
Design a class to find the `kth` largest element in a stream. Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Implement `KthLargest` class:

- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `kth` largest element in the stream.


### Example 1:
```
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```


### Solution
Since we want to find k largest, we can utilize a heap. Since we want to find largest what we use a max heap to store only k elements. That means our heap would always have the top k elements inside it. If we consider the example and look at the `nums`, our heap would something like this:
```
  8
 / \
4   5
```
At this point what we want to return is `4` but we can't easily get `4` from this as we would have to traverse and find the smallest one. But since we want to find the smallest out of the top k elements, we can use a min heap instead:
```
  4
 / \
8   5
```
Now our root would always be the `kth` largest so we can just do `heap[0]` to get the root then.

Now we when adding new values to our heap we have 2 cases to handle:

Our heap does not already have `k` elements inside it
- Then we can simply add the value to our heap

Our heap is full, and we want to add a new value
- We would add the new value IF it is larger than our root (the smallest of the top k elements)
- If this is the case we would pop from heap (only `k` elements allowed) and add our new value

We only add the value if it's larger than our root because we want to store the top `k` elements. Our heap represents this. Suppose we have `[4,8,5]`, and we want to add `9`, by looking at it we would get rid of `4` because right now `4` would be the `4th` largest: `9,8,5,4` so it is no longer one of the top `k` elements.