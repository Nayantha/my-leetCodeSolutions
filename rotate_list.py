# https://leetcode.com/problems/rotate-list/
from typing import Optional

from list_node import ListNode


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(next_node=head)
    for i in range(k):
        previous_node = dummy
        head = dummy.next
        while head.next:
            head = head.next
        previous_node.next = None
        head.next = dummy.next
    return dummy.next
