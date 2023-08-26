# https://leetcode.com/problems/rotate-list/
from typing import Optional

from data_structures.list_node import ListNode


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return head
    length = 1
    curr = head
    while curr.next:
        length += 1
        curr = curr.next
    # set the next pointer of original list's tail to original list's head
    curr.next = head
    k = length - k % length
    while k > 0:
        k -= 1
        curr = curr.next
    new_head = curr.next
    curr.next = None
    return new_head
