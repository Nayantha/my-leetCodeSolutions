# https://leetcode.com/problems/rotate-list/
from typing import Optional

from data_structures.list_node import ListNode


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(next_node=head)
    for i in range(k):
        previous_node = dummy
        current_node = head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        current_node.next = dummy.next
        dummy.next = current_node
    return dummy.next
