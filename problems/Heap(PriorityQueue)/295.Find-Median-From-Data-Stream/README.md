# Problem

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for `arr = [2,3,4]`, the median is `3`.
For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the `MedianFinder` class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

### Example 1:

```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

### Solution

If we consider a sorted array like `[1,2,3,4]` or `[1,2,3,4,5]` we can split the array into two halves:

- `[1,2]`, `[3,4]` and `[1,2,3]`, `[4,5]`

Looking at this when we have an even amount the median is the average of the top of the first half and the bottom of the second half. First half has `2` on top and second half has `3` on bottom so median is: `(2 + 3) / 2 = 2.5`

When there is an odd amount, the median is the top of the half with more elements in it. Since first half has one more element in it the median is `3`.

Since when numbers are added they are not guarnteed to be in order, we can use 2 heaps keep track of the 2 halves. For the first half, since it stores the smaller elements in the array and what we want to is the top of the first half we will use a max heap. Since the finding median requires sorted array, the top of the first half will be the largest out of all the other numbers in this half. Same applies for the second half, since it stores the larger half of the numbers we will use a min heap instead. Since for the second half we are interested in the bottom of this half, this value will be the smallest out of all the elements in this half.

Now when adding to the 2 heaps, we will always make sure that the first half will always have more or equal the number of elements as the second half. This way when we have an odd amount of numbers we will know that the first half will contain the median. Now when the current amoutn is even we should add to first half as adding new element will make current amount and odd number and we want the first half to have more or equal the number of elements. Otherwise we will add it to the second half.

When adding new numbers we don't know the what values they are so the heaps may end up out of order. If we add 2 nums in this order: `6, 5`. Our heaps would like this

- first half: `[6]` second half: `[]`
- first half: `[6]` second half: `[5]`

But we want the values in sorted order like: `[5,6]`, what we need to do is swap both of the values, move `5` to first half and `6` to second half. So when we add to second half if the top of heap is smaller than top of first half we will swap. When we add to first half we will also swap when the top of first half is larger than top of second half.
