# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional

from add_two_numbers import ListNode


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy_node = ListNode(0, head)
    left_previous_pointer, curr = dummy_node, head
    for i in range(left - 1):
        left_previous_pointer, curr = curr, curr.next
    prev = None
    for i in range(right - left + 1):
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node
    # now curr is the node at position (right + 1), prev is pointing at the node at position right
    left_previous_pointer.next.next = curr
    left_previous_pointer.next = prev
    return dummy_node.next
