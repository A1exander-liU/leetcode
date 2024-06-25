# Problem
You are given an array of `k` linked-lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked lists


### Example 1:
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

### Example 2:
```
Input: lists = []
Output: []
```

### Example 3:
```
Input: lists = [[]]
Output: []
```


### Solution
Since we have variable amount of lists to merge together we can utilize a min-heap (priority queue): always returns the next smallest item in the heap.
Because it always returns the next smallest item, we could get it all in ascending order by just continusly removing from the heap. But all the elements are part of different linked lists, so first need to add them all to an array first then we can turn it into heap. After getting every single element, just need to keep removing from the heap until is empty.