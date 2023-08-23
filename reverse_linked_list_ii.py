# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional

from add_two_numbers import ListNode


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    prev, current = None, head
    current_position = 1
    temp_head = head
    while temp_head:
        next_node = temp_head.next
        if left <= current_position <= right:
            temp_head.next = prev
        elif current_position > right:
            break
        current_position += 1
        prev = current
        current = temp_head.next
        temp_head = next_node
    return head
