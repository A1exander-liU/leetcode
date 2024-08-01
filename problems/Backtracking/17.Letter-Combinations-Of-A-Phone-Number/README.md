# Problem

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

### Example 1

```bash
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Example 2

```bash
Input: digits = ""
Output: []
```

### Example 3

```bash
Input: digits = "2"
Output: ["a","b","c"]
```

### Solution

Use a map to store the combos for each number: `{ "2": "abc", ... }`. We find solution once length of current string is same as length of
`digits` since we need to find combos of choosing one letter in each digit group. We can use a index to keep track of current group we are adding from, we start from `0` and each time we add a digit from current group we would increment by `1` so next digit added would be part of the second digit group. Then we just need to iterate over all letters of current digit group and then use the index to move on.

- `phoneMap[digits[numIndex]]` to get digits for current group
- then do `numIndex + 1` we moving on

```

```
