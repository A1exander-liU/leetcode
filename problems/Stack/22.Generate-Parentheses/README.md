# Problem
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 
### Example 1:
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

### Example 2:
```
Input: n = 1
Output: ["()"]
```


### Solution
1. want to find all ways to make valid parantheses with `n` pairs of them
2. if we have `n` pairs it means we have `n` opening and `n` closing parentheses
   - this also means the length of each string has to be `n * 2` (`n` opening + `n` closing)
3. so when do can do have a valid parantheses as we are building it say our `n` is 3?
   - for the starting one, it always has to be a opening one cause you cant have `)(`, you need an opening and at some point a matching closing as well
   - so we know we have to start with a `(`
   - so after a `(` what can we have?
     - can we have another `(`? yea `((`, we have open count of 2 which is not greater than 3 (`n` is 3, remember if we can have `n` opening and closing)
     - can we have a `)` now? yea, we can close the first pair `()`, now we have 1 open and 1 close
     - `()`, can we add a `)` `())`, nope it's not valid because we needed a `(` first
       - if we do this we would have open count 1 and close count 2
       - note that we have invalid when the close count > open count
       - makes sense since to have a `)`, we first need a `(` to pair with it, if the close count is more than open count, we dont have enough `(` to pair
       with a `)`
     - `()` we can add `(`: `()(`
   - note that we have like a binary tree here, we start with `(` as the root and each time we can only make 2 choices: add a `(` or `)`

```
              (
           /     \
          ((      ()
         /  \    /  \                  
       ((( (()  ()(    <- the right is empty here because adding a ')' is invalid

```
4. so basically we are building a binary tree, where the leaf nodes (no children are the answers)
5. we start at `(` every time we build a left and right, left in this case would be adding a `(` and right would be adding `)`
   - if adding a `(` or `)` would be invalid, there would be no right or left child
   - once we hit the very end of building (if the current string length == `n * 2`, because of `n` opening + `n` closing), we can add this to our result list
   - we can implement using recursion or iterative
   - with iterative we will use a stack to keep track of the visited nodes so we can go back if we reach the end of one