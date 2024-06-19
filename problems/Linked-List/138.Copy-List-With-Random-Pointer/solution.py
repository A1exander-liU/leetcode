from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return

        # also keep None when tracking relationships, random may pont to null
        hashmap = {None: None}

        # handle head node first to start linked list
        new_head = Node(x=head.val)
        hashmap[head] = new_head

        if head.next not in hashmap:
            hashmap[head.next] = Node(x=head.next.val)

        if head.random not in hashmap:
            hashmap[head.random] = Node(x=head.random.val)

        new_head.next = hashmap[head.next]
        new_head.random = hashmap[head.random]

        current = head.next
        while current is not None:
            if current not in hashmap:
                hashmap[current] = Node(x=current.val)

            current_copy = hashmap[current]

            if current.next not in hashmap:
                hashmap[current.next] = Node(x=current.next.val)

            if current.random not in hashmap:
                hashmap[current.random] = Node(x=current.random.val)

            current_copy.next = hashmap[current.next]
            current_copy.random = hashmap[current.random]

            current = current.next

        return new_head
