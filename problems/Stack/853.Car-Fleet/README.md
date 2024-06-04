# Problem
There are `n` cars going to the same destination along a one-lane road. The destination is `target` miles away.

You are given two integer array `position` and `speed`, both of length `n,` where `position[i]` is the position of the `ith` car and `speed[i]` is the speed of the `ith` car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.


### Example 1:
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
```

### Example 2:
```
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
```

### Example 3: 
```
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
```


### Solution
Basically each car will travel `speed` amount per unit of time until they reach `target`.
So if a car has `position` 8 and `speed` of 2, they will move 2 each time all the way to `target`: 8 -> 10 -> ... -> `target`

Also a car can't pass another car meaning that if one car starts before another one they can never get in front of the slower car
Car1: `posiiton`: 0, `speed`: 4
Car2: `position`: 5, `speed`: 1

Car1: 0 -> 4 -> 8 *can't do this
Car2: 5 -> 6 -> 7

Car1: 0 -> 4 -> 7 -> 8 *Car1 is now matching the slower car it would have passed (speed matches the slower Car 2)
Car2: 5 -> 6 -> 7 -> 8

Car1 will end up passing Car2 but this is not allowed, the faster car (Car 1) will have to match the speed of slower car (Car 2) it would have passed

1. One useful thing to do is calculate how long it would take a car to reach the `target`
   - `(target - position of car) / speed of car`
   - if `target` is 12 and `position` is 8, then the car only need to move 4 units, if their `speed` is 2, it would take them 2 units of time to finish
2. You can sort their positions and keep track of each of their time. here first element is position and second one is the time it takes them
```
(0, 12.0)
(3, 3.0)
(5, 7.0)
(8, 1.0)
(10, 1.0)
```
- for the first car it takes them 12 units of time, its super slow and never passses any other car
- but note the second and third car, second car starts at 3 and finishes in 3 units of time, third card starts at 5 and finishes in 7 units of time
  - here even though second car started earlier than the third car it finished before it, this means it would have passed the third car
  - so second car was actually faster than the third car
  - but the faster car has to match the slower car, so it would end up being blocked by the third car (meaning they would both finish at same time, second and third car would be one fleet)
  - this also means that a slower car further ahead would block all faster cars that started behind it
- now for fourth and fifth car, they both finish in 1 unit of time, since they both finish at same time they are part of same fleet
- so basically the cars that block end up being a fleet
3. using the idea of a slower car further ahead would block all faster cars before we can build a monotonic stack (all elements are ordered in asc or desc)
   - what we can do is iterate over out sorted cars and add them to the stack
   - we will keep removing cars from the stack if they are faster or same than the current car
     - this way we are only storing the cars that would end up blocking the other cars (slower cars block faster cars)
     - also accounting for when they finish in same time they are part of same fleet
   - since we end up only storing the cars that block we can just return the length of the stack

