# Problem
Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√(x1 - x2)2 + (y1 - y2)**2`).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


### Example 1:
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

### Example 2:
```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```


### Solution
Since we want to find the `k` closest we would need to have heap of all our points and then pop out `k` of them back into a result array. As we want to find closest, we should use a min heap as shorter distance from origin means closer points. 

The distance would be: `sqrt(x**2 + y**2)`, since we want to find distance from origin our second point would be `(0,0)`, so we need to subtract as it would not change the value (since origin is just 0). Because we want to pop from heap based on the distance but also want to return the points we should use a tuple to store the distance and the point: `(distance, point)` this way it compares using distance and we can get our point back. 

So we just need to caculate the distance of each point and add them all as tuples. Then all we need to do is pop `k` times from the heap and store the points in a result array.

Additional optimizations are not calculating the squareroot since this relativly expensive operation, we only need to know the closest points so are concerned with the actual values of the distance. If you consider `sqrt(10)` and `sqrt(9)`, we know `10` would be higher as higher number would have a larger square root.

Furhter optimization is not using a heap but sorting instead. With heap you need `O(n log(n))` to add all points to heap and then `O(k log(n))` to pop our `k` points. But with sorting all you need is `O(n log(n))` to sort and then `O(n)` to splice the list to get the first `k` elements:
```python
return sorted(points, key=lambda point: point[0]**2 + point[1]**2)[:k]
```
