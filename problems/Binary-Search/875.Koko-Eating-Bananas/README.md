# Problem
Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.


### Example 1:
```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

### Example 2:
```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

### Example 3:
```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```


### Solution
First we need to know how to calculate how long it would take Koko to eat all piles for any `k`.
- we can do `math.ceil(pile / k)`
- since she can eat `k` per hour, dividing `pile` by `k` would be how many hours it would take to finish
- we also round up because the hour has to be an integer (can't take 3.5 hours, have to round up to 4 hours)
- since this is for a single pile we can simply loop through all piles and add the eat_times together

Note that we won't search through the `piles` array using binary search. What we want to find is not in the `piles` but the eating speed `k`.
So we don't use `piles` then what do we use to perform binary search on then? We use the range of possible `k` values.
In normal binary search left and right at start represent the min and max values of the search space, so what are the min and max values of `k`?
- min `k` has to be 1, can't be 0 otherwise Koko would never finish the bananas since she would never eat
- max `k` should be `max(piles)`, 
  - in the description it says that if she can finish a pile but still have leftover, Koko will not eat more
  - if `k` is 20 and `piles` are like `[10, 5, 20, 20]`, if she eats pile of 10 she will not eat anymore during the hour
  - this means that **she will eat one pile at most**
  - if she will eat one pile at most max should be just the largest pile so she can finish one pile each hour
  - anything more than largest pile would be a waste for `k` since it would change how long it would take to finish all piles at that point


Now we need to figure out when to move left or right. Since we need to find a min value of `k` so she can finish all piles within `h` hours,
we should compare how long it takes to finish all piles for given `k` against `h` hours.

If for our value of `k` the eat time we got was more than `h` hours that means Koko was eating too slow, so `k` was actually too small. Since `k` is too small we need to move left side to get bigger `k`

Now if the eat time is less than or equal to `h` hours that means it is a good `k` (for `k`  eat time needs to be within `h` hour), but not the best. we want it to be as close to `h` hours as much as possible. so if our eat time was smaller, than we need to move right side to get smaller `k` because the eat speed was too fast. at this point we should also find the min `k` since right now `k` is valid value since eat time is less than `h`.

we keep the min value because we want to minimize `k`, if is too small it would take longer than `h` hours to eat (wouldn't hit the `eat_time <= h` since did not finish within `h` hours), if it is same as `h` then it is almost perfect, but if `k` is too big it would take a very short time to finish all.

```python
if eat_time <= h:
    k = min(k, new_k)
    right = new_k - 1
```