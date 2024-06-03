# Problem
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.


### Example 1:
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

#### Example 2:
```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```


### Solution
so checking if permutation of `s1` in `s2` means that any ordering of `s1` is a substring of `s2`
1. so to compare if substring contains a permutation we can count character frequencies
   - since it is just reordering we can track if the current substring has the correct characters and counts (use dictionary)
2. since we need to make sure if its a substring, we have to stop moving the `right` pointer when we find a character that doesn't exist in `s1` or
that we have too much of one of the characters in `s1`.
3. will have to move `left` pointer when one doesn't exist or we have too much of one character
   - instead of just removing the character from dictionary we subtract 1 from the count and remove when count is 0
   - we do this to preserve the substring, we want to make sure character counts matches with our substring
4. during each iteration we can compare if our current character count matches the character count of `s1` (to determine if the substring exists)
 