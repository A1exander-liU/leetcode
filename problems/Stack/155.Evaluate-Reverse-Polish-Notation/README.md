# Problem
You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

**Note** that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

### Example 1:
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```
### Example 2:
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

### Example 3:
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```


### Solution
Looking at the examples, everytime we see an operation we will apply it to the latest 2 numbers. In `["4", "13", "5", "/", "+"]` we do `13 / 5`. We need to maintain all the numbers we have as we get them.

1. when we first encounter operation we have `["4", "13", "5"]` in list and see `"/"`
2. so we have division operation and we know that when we see an operation we do it on the latest 2 numbers. 
3. we can just pop 2 times to get the 2 latest numbers: `"5"` and `"13"`
   - note that first pop will be `"5"` and second pop will be `"13"`, so when we do the calculation (division in this case) we have to reverse the order of the variables
   - so we do `13 / 5 = 2`
4. now we have only `"4"` in the list, note that the next operation is a `"+"` for `4 + 2`
5. since we just calculated the `13 / 5` that is needed for the next operation, we need to add `"2"` to our list. 
   - every time we compelete an operation we need to add the result back to the list
6. now we have `["4", "2"]` so when we find `"+"` we can pop off `"4"` and `"2"` and get final result of `"6"`
7. remember that we said we add result of operation to our list so at end we will have only `["6"]`, so the only element left is the final answer