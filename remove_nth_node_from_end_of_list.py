# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional

from add_two_numbers import ListNode


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    left_pointer = dummy
    right_pointer = head
    while n > 0 and right_pointer:
        right_pointer = right_pointer.next
        n -= 1
    while right_pointer:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next
    left_pointer.next = left_pointer.next.next
    return dummy.next
