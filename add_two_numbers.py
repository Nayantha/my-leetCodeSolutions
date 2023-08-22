# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    remainder = 0
    while l1 and l2:
        l1 = l1.val + l2.val
        l1 = l1.next
        l2 = l2.next
    if l2 and not l1:
        l1 = l2
    return l1
