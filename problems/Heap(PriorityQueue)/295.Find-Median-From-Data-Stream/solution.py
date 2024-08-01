import heapq


class MedianFinder:
    """
    if we consider sorted array: [1,2,3,4] or [1,2,3,4,5]
    can split into 2 lower and upper half
    - [1,2] [3,4] or [1,2,3] [4,5]
    - that means if even amount in total: median is average of top of lower half and bottom of upper half
    - that means if odd amount: median is top of lower half
    - we can then use heaps to store this information
    - max heap for lower half and min heap for upper half

    - when there are equal amount add to left side (max heap) otherwise add to right side (max heap)
      - left side will always then have more or equal the number of elements in right side
    - if there equal amount: median is average of the top of left side and right side
    - if there is unequal amount: median is top of left side

    for maintaining that left side contains first half and right side contains the next half
    - there can be no element in left side larger than right side
    - there can be no element in right side smaller than left side
    - because the min and max heaps store half of each side, the top of the heaps represent the values in the middle
      - so if the values in the middle are not in sorted order we have to swap them to make sure they are

      when adding to left side:
      - swap the top of both sides if top of left side is larger
      - our array would look like: [1,2,7,4,5] -> [1,2,7] [4,5] which is not in sorted order

      when adding to right side:
      - swap the top of both sides if top of right side is smaller
      - our array would look like: [1,2,0,5] -> [1,2] [0,5] which is not in sorted order

    [6] []               add 6 to left side, even amount
    [6] [10]             add 10 to right side b/c uneven amount, no swap b/c its bigger than 6
    [2,6] [10]           add 2 to left side, even amount
    [2,6] [6,10]         add 6 to right side, uneven amount
    [2,5,6] [6,10]       add 2 to left side, even amount
    [2,5,6] [0,6,10]     add 0 to right side, uneven amount, swap b/c 0 is < 6

    1 2 3
    [1] []
    [1] [2]
    [1,3] [2] -> []
    """

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            heapq.heappush(self.max_heap, -num)

            if self.min_heap and self.max_heap and -self.max_heap[0] > self.min_heap[0]:
                left = -self.max_heap[0]
                right = self.min_heap[0]

                heapq.heapreplace(self.max_heap, -right)
                heapq.heapreplace(self.min_heap, left)
        else:
            heapq.heappush(self.min_heap, num)

            if self.min_heap and self.max_heap and self.min_heap[0] < -self.max_heap[0]:
                left = -self.max_heap[0]
                right = self.min_heap[0]

                heapq.heapreplace(self.max_heap, -right)
                heapq.heapreplace(self.min_heap, left)

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
