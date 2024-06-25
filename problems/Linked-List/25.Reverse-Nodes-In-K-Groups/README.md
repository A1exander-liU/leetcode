# Problem
Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


### Example 1
```
Original
[1 -> 2] -> [3 -> 4] -> 5

Reversed
[2 -> 1] -> [4 -> 3] -> 5

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

length of linked list was not multiple of k, so the leftover 5 is not reversed
nodes are reversed in their own groups
```

### Example 2
```
[1 -> 2 -> 3] -> 4 -> 5

[3 -> 2 -> 1] -> 4 -> 5

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

the leftover 4 -> 5 could not form group of `k` so not reversed
```


### Solution
General idea is to reverse only `k` nodes each time by keeping a counter and resetting each time you hit `k`. But when you are reversing you also have to make sure you don't reverse nodes that aren't enough to make a group of `k`, in example 2, the `4` and `5` are not reversed. To make sure, you can only reverse the amount of groups that are possible: if there are 5 nodes, and `k` is 2 only 2 groups are possible (`5 // 2 = 2`), to do this we need one pass in the begginning to count the number of nodes. Then everytime we can keep a counter for number of groups created and stop once we hit the max groups possible.

Since it is being reversed, the `head` will change if you can reverse a single group, the new head should always be the last node of the first group. `1 -> 2` and `1 -> 2 -> 3` are the first groups in both examples, since it is reversing the last node will be the first node. Now you also need to handle linking the reversed groups together, for example 1, `[2 -> 1] -> [4 -> 3]`, we need to point the last node of the group (which was originally the first node, so should keep a variable to track this before we reverse the group like `group_head`) but after we reverse the first group, the second group hasn't been reversed yet so it is: `[2 -> 1] -> [3 -> 4]`, so we need the second group to be reversed first. What we can do is track the previous group's last node (`group_head`) so once we finish the group after it, we can update the `next` pointer of the group before it to be last node of the not yet unreversed group.

The last node (`group_head`) of the final group will have to point to the start of the leftover nodes, so in example 1 the `3` should point to `5` which we can just do by updating the previous group head's `next` pointer. 