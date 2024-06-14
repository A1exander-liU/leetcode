# Problem
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

- `TimeMap()` Initializes the object of the data structure.
- `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

Constraints:

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits.
- `1 <= timestamp <= 107`
- All the timestamps `timestamp` of `set` are strictly increasing.
- At most `2 * 10^5` calls will be made to `set` and `get`.


### Example 1:
```
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
```


### Solution
So for the problem you want to store the key and it values and timestamps in some way.
For actually getting something back it should look for the all timestamps related to that key and get the biggest timestamp that is <= to the provided timestamp. If you have "foo" key with timestamps of 1 ("bar") and 4 ("bar2") and you want to get the value of this key at timestamp 3: `get("foo", 3)`,
you should return back `"bar"`. Since you only have 1 and 4, 1 is timestamp that is closest to 3 but still is <= 3, but 4 is greater so no. Basically you want to get the closest timestamp that is before or at the provided timestamp.

In the constraints there is one very important one: All the timestamps `timestamp` of `set` are strictly increasing. This means that the timestamps for any key are **gaurunteed** to be in ascending order. So if u add 1 in start, next one has to be bigger than 1 and so on. Basically the timestamps are already in ascending order so we can perform binary search on it. (Can use binary search because we are trying to maximize, minimize or find a certain value from a sorted input array or a range of values)

There are some cases to handle like what to do when we find a timestamp greater than the target?
- we should move the `right` because if the timestamp is too big we need to find a smaller one (timestamp <= target)
Now when the timestamp is less than target we still are not done since we want to find the biggest one that is still less than or equal to the target
- since we want to find the biggest that is less than or equal to it, we should move `left` to see if we can get a bigger one
- note that the less than and equal check are combined together because we want to keep going to see if we can bigger one still


```python
while left <= right:
  mid = left + (right - left) // 2

  if timestamps[mid] <= target:
    left = mid + 1
  else:
    right = mid - 1

return value of timestamps[right] but if right == -1 return ""
```

we also don't need to calc max everytime when our timestamp is less than or equal to the target, we can use the `right` index
- since we keep going until `left` goes pass `right`, `left` will alwayvs be invalid index and tht `right` will always be the last index of the
timestamp that is less then or equal to target
- we know it will be the greatest since if we got a smaller timestamp we would keep moving the `left` each time, if our target is 5 and our current `mid` is at 4 we would move the `left` again to see if we can get a closer one (meaning 5), if during the next iteration we ended up searching through everything, since `right` was not updated, the previous time it still points at the last valid place. 
- also note that when we return `right` we have to make sure it is not `-1`, this would happen if we kept moving right each time, meaning that all timestamps were greater than target and we had no timestamp that was <= target

now we need to figure out how to store the stuff. a good choice to start is use hashmap to store the keys but what should we store as the value.
since each key can have multiple values we can't just store a single value and since we need to search through timestamps, we will need to store an
array of the timestamps. we also need to store the corresponding value of each timestamp as well since `get` returns the value. you can do this in different ways like instead of storing timestamps in array you use a tuple of the timestamp and the value instead or can use nested dict to store the timestamps separately and having individual keys for timestamp to value

```python
# using tuple
{ "foo": [(1, "bar"), (4, "bar2")] }

# using nested dict
{ "foo": { "timestamps": [1, 4], 1: "foo", 4: "bar2" } }
```