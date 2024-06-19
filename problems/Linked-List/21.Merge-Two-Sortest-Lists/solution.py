from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        i = list1
        j = list2

        sorted_list = None

        if i.val <= j.val:
            sorted_list = i
            i = i.next
        else:
            sorted_list = j
            j = j.next

        current = sorted_list
        while i is not None and j is not None:
            if i.val <= j.val:
                current.next = i
                current = current.next
                i = i.next
            else:
                current.next = j
                current = current.next
                j = j.next

        while i is not None:
            current.next = i
            current = current.next
            i = i.next

        while j is not None:
            current.next = j
            current = current.next
            j = j.next

        return sorted_list
