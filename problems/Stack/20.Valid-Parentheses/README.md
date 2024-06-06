# Problem
Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


### Example 1:
```
Input: s = "()"
Output: true
```

### Example 2:
```
Input: s = "()[]{}"
Output: true
```

### Example 3:
```
Input: s = "(]"
Output: false
```

### Solution
We want a matching closing bracket at the right time. If we have `())`, the first 2 brackets match but then we are left with closing bracket with nothing. need way to keep track of what we are matching, can use stack to keep track. can keep adding each bracket we find and remove the top 2 when we have a opening and closing match

`()()` 
1. can start by adding `(` to stack
2. then add `)` to stack
3. whenever we add a closing bracket, we need a opening bracket before it or else it would not be valid (because we are matching as we go, the string as whole can be like this `((()))`)
4. because its valid we remove the top 2 elements: `(` and `)`
5. now if we have invalid when going through our algo: `((())))`, at the end our stack would have a single `)` inside
   - using this can check if length of stack at the end to determine if order was valid (if there was brackets still inside it means there wasn't matching opening or closing so its invalid)
 