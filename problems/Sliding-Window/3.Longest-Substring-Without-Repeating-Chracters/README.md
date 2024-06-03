# Problem
Given a string `s`, find the length of the longest substring without repeating characters.


### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```


### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```


### Solution
1. need to figure out when to move the `left` or `right` pointer of the window
2. we keep moving the `right` pointer until there is a duplicate
   - can use `set` to track current `substring`, if we add a dupe to a `set`, the `length` won't change
   - can check if `length` changes after adding a `new character`, if no change then `new character` already appeared
3. when there is dupe we need to move the `left` pointer until there is no dupe
   - since the `new character` will be the dupe, keep moving `left` pointer until the `new character` is not part of current string
   - can check the `set` if `new character` still in string, if it is we just keep removing the character at the `left` pointer
4. with using the `set` to track current string, can comapre `length` of `set` each time against global max to keep track of the longest