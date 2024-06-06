# Problem
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

### Example 1:
```   #
    @ @
    @ @
    @ @   #
#   @ @ # #
# # @ @ # #

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the @, which has an area = 10 units.
```

### Example 2:
```
  #          #        @
  #          #        @ 
# #        @ @      # @
# #        @ @      # @

Input: heights = [2,4]
Output: 4
There are 2 ways here to get an area of 4
```
### Solution
```
          #
#         #  
#     #   #
# #   # # #
# #   # # #
```
what stack is like at start of each iteration
for each height, we need to find the next and prev height that is smaller than it
- this waywe know how far the rectangle for this height will extend from
- if we look at height 3 (index 3) in this example
  - the prev smallest is height 0 (index 2)
  - next smallest is height 2 (index 4)
  - so basically the rectangle of height 3 has a width of 1  
- key idea: at each height find the prev and next smallest
  - this way we know how far the rectangle of this heigt will extend
  - say height is 4 and we want to find a rect of height 4
    - say that prev smallest is at index 2 and next smallest is at index 5
    - thismeans that everything between index 2 and 5 has a height of 4 or greater
    - using this we know we can have a height 4 rectangle from index 3 to 4 (which is width of 2)

- key thing: finding prev smallest and next smallest
  - naive:look at each height just before the current height every time
    - slowbecause we are recalculating everytime

    - can use previous results instead of traversing all heights before or after
      - `prev_smallest[i]` or `next_smallest[i]` means that for `ith` height in `heights` array, it index that is prev smallest or next smallest is 
        `prev_smallest[i]`/`next_smallest[i]`
    - `heights:       [2,1,5,6,2,3]`
      `prev_smallest: [-1,-1,1,1,..,..]`

      say we are trying to find prev smallest at index of 4, we compare height at current index with previous index
      so we check if 6 < 2, so height just before it is bigger than 2, now we can jump to where `prev_smallest[p]`
      is. this works because we track the prev smallest for each height. 6 points to index 1 which means this is the index which is the prev smallest of 6.            this also means that everything between index 1 and the index where 6 is, is greater than 6, so it is also bigger than 2 meaning we can skip redundant traversals since we know everything in between is greater than or equal to 6. so we just keep jumping indices until we find the smaller height.

    ```python
    prev_smallest = [-1] * n
    next_smallest = [n] * n
    
    while p >= 0 and heights[p] >= heights[i]:
        p = prev_smallest[p]
    prev_smallest[i] = p

    while s < n and heights[s] >= heights[i]:
        s = next_smallest[s]
    next_smallest[i] = s
    ```