from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def add_digits(d1, d2):
            val = d1 + d2
            return val % 10, val // 10

        num1 = l1
        num2 = l2

        val, carry = add_digits(num1.val, num2.val)

        result = ListNode(val=val)

        num1 = num1.next
        num2 = num2.next
        current = result
        while num1 and num2:
            val, carry = add_digits(num1.val + carry, num2.val)

            current.next = ListNode(val=val)

            current = current.next
            num1 = num1.next
            num2 = num2.next

        while num1:
            val, carry = add_digits(num1.val, carry)

            current.next = ListNode(val=val)

            current = current.next
            num1 = num1.next

        while num2:
            val, carry = add_digits(num2.val, carry)

            current.next = ListNode(val=val)

            current = current.next
            num2 = num2.next

        if carry:
            current.next = ListNode(val=carry)

        return result
