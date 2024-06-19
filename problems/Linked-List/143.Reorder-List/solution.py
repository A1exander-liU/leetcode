from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return

        q = deque()
        current = head.next
        while current is not None:
            q.append(current)
            current = current.next

        current = head
        while q:
            if len(q) > 1:
                right = q.pop()
                left = q.popleft()

                current.next = right
                right.next = left
                left.next = None

                current = left
            else:
                right = q.pop()

                current.next = right
                right.next = None

                current = right
