# Problem
Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

`MinStack()` initializes the stack object.
`void push(int val)` pushes the element `val` onto the stack.
`void pop()` removes the element on the top of the stack.
`int top()` gets the top element of the stack.
`int getMin()` retrieves the minimum element in the stack.
You must implement a solution with `O(1)` time complexity for each function.


### Example 1:
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```


# Solution
1. key thing here is keeping track of the minimum value, if we just have a variable to find min each time new element is added won't work
   - what if the min `val` is removed? which do choose as next min? can't just search through, cause we need `O(1)` time complexity
2. instead of storing just a variable we can keep track of of the minimum for each node
   - when we add a new `val`, we also add the min value currently with it
   - compare the current `val` to be added with the previous `val` item, this way we can keep track of the min as we go
   - why it works? the min val for each element has to be an element before it because if element after was smaller but is removed, it won't be the element's min anymore