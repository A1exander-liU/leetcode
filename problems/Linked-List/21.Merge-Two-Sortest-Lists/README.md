# Problem
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


### Example 1:
```
list 1: (1) -> (2) -> (4)
list 2: [1] -> [3] -> [4]

[1] -> (1) -> (2) -> [3] -> (4) -> [4] 

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Example 2:
```
Input: list1 = [], list2 = []
Output: []
```

### Example 3:
```
list 2: [0]

[0]

Input: list1 = [], list2 = [0]
Output: [0]
```


### Solution
This is basically the final step of merge sort, when you 2 arrays in sorted order and you want to combine them together by continously adding the next
smaller element from the 2 lists.

In regular merge, we use while loop to keep going until one of the sorted array runs out of elements (if one array runs out we can't compare the smaller element between the 2 arrays). At each point we add the smaller element and move the index of the array with the smaller element forward. Since we are using linked list and not array, to update our result with the next element we have to update the `next` pointer instead.

What we want to do is first is initialize our head node. Since we want it in ascending order, we should pick the one with smaller value. Afterwards we utilize `current` to iterate and add the next node by updating the `next` pointer.
If use example 1, we would start with head node of `1` of `list2`, so next we would compare `1` from `list1` and `3` from `list2`.

```python
# head = [1]

# i is for list1, j is for list2
if i.val <= j.val:
  current.next = i # [1] -> (1) now we would've 'added' the next node
  current = current.next # our next node was (1), current should now be next one since now we want to update this new added node's next pointer
  i = i.next # to move to next element
else:
  current.next = j.val

  j = j.next
```

Like with regular merge, when one array runs out, we need to add the rest of the elements in the other array
```python
# if j reached end of list (j became None) add rest of i to the new list
while i is not None:
    current.next = i
    current = current.next
    i = i.next

# if i reached end of list (i became None) add rest of j to the new list
while j is not None:
    current.next = j
    current = current.next
    j = j.next
```