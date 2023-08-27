# https://leetcode.com/problems/partition-list/
from typing import Optional

from data_structures.list_node import ListNode


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    left, right = ListNode(), ListNode()
    left_tail, right_tail = left, right
    while head:
        if head.val < x:
            left_tail.next = head
            left_tail = left_tail.next
        else:
            right_tail = head
            right_tail = right_tail.next
        head = head.next
    left_tail.next = right.next
    right_tail.next = None
    return left.next


def partition_ii(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    ...
