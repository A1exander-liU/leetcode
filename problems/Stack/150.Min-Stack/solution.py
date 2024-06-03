from math import inf


class MinStack:

    def __init__(self):
        self._items = []
        self._min = inf

    def push(self, val: int) -> None:
        if not self._items:
            self._items.append((val, val))
        else:
           prev, prev_min = self._items[-1]
           self._items.append((val, min(val, prev_min)))
        

    def pop(self) -> None:
        val, _ =  self._items.pop()
        return val
 
    def top(self) -> int:
        val, _ = self._items[-1]
        return val
        

    def getMin(self) -> int:
        _, min_val = self._items[-1]
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# storing the min with item is better than variable for the min val since you have the history of min vals
# also an item's min val will have to be itself or a value added before it since if the item after it is smaller but removed it can be this item's min anymore

# (-2,-2), (0,-2), (-3,-3)
# current min: -3
# pop()
# (-2, -2), (0, -2)
# current min: -2
#