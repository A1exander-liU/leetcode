# Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
### Example 1:
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

### Example 2:
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3:
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```


### Solution
What we are basically doing is adding the 2 number digit by digit. Looking at example 1, the first digits are `2` and `5` so we add them up `2 + 5 = 7`; our first node in the result list will be `7`. Next we add `4` and ``6`: `4 + 6 = 10`, when we add these like we normally do when writing we have to carry the `1` over to the next digit place and we keep the `0`. So our next node would be `0` and the `carry` would be used in the addition: `1 (carry) + 3 + 4 = 8`, so final node is `8`. 

Now when we add 2 digits how do we determine what is the `carry` and what is `val` for current digit place. Can use modulus and integer division to get them. If we have something like `18`, `carry` would be `1` and `val` would be `8`. To get the `carry` we can do `sum // 10`, this is basically extracting the second digit of the number which is what we want: `29` would `2`, `19` would be `1`. To get the `val` we would do `sum % 10`, `4 % 10 = 4, 10 % 10 = 0`.

Now we know how to get `carry` and `val`, notice that `carry` is always used for next digit place whether its `0` or `1`, that means every time we add, we should keep track of the `carry` for the next digit place. 

Now when we add, we are adding the digit from first list with digit from second list each time, but the lists do not have to be the same length, we can do: `100 + 99`, these are same length. So when we are adding we have to make sure both lists still have a node, we have to stop if one list runs out. In example 3, `9999` runs out and we are left with `999` from longer list. So basically if a list runs out we just add the remaining numbers from the other list, So instead of doing: `carry + num1 + num2`, we just do `carry + num1`.

One final case is if last addition results in carry, if you have `7` and `3` at the end we have be left with `carry` of 1 so we need to make sure if there is a carry at the end, we add one more node with the `val` as the `carry`.