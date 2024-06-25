from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
                group_head, group_tail?
                counter till reach k
                current pointer

                [1 -> 2 -> 3] -> 4 -> 5
                1 <- 2 <- 3  4 -> 5
                |____________^

                head should be changed to head of first group if enough nodes

                have group_head, keep moving forward until k or end reached
                - if didnt hit k, don't reverse
                - if hit k, go from group_head and start reversing
        ,
                if we iterate over to count for k then go back to iterate to reverse, its kinda slow?
                 - maybe have one pass in start to find out list size to do: size // k to get number of groups
                 - then can keep reversing until that many groups

                group head should point to node after group_tail

                if group is not first group, the prev_node should point to group_tail
                group_head -> next node
                prev_node -> group_tail (if not first group)
        """
        current = head
        n = 0

        while current is not None:
            n += 1
            current = current.next

        total_groups = n // k
        group_counter = 0

        new_head = None

        current = head
        prev = None

        group_head = head
        prev_group_head = None

        while group_counter < total_groups and current is not None:
            group_head = current

            prev = None
            for i in range(k):
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            # new head should be last element of the first reversed group
            if group_counter == 0:
                new_head = prev

            if prev_group_head:
                prev_group_head.next = prev

            prev_group_head = group_head

            group_counter += 1

        prev_group_head.next = current

        return new_head
