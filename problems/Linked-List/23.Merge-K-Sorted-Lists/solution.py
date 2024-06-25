from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        min_heap = []
        entry_count = 0
        for head in lists:
            if head is None:
                continue

            current = head
            while current:
                min_heap.append((current.val, entry_count, current))
                current = current.next
                entry_count += 1
        heapq.heapify(min_heap)

        head = heapq.heappop(min_heap)[2] if min_heap else None
        current = head
        while min_heap:
            current.next = heapq.heappop(min_heap)[2]
            current = current.next

        return head
