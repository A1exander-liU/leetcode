from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        current = head
        while current is not None:
            nodes.append(current)
            current = current.next

        remove_index = len(nodes) - n
        node_to_remove = nodes[remove_index]

        if node_to_remove is head:
            head = head.next
        else:
            prev_node = nodes[remove_index - 1]
            prev_node.next = node_to_remove.next

        return head
