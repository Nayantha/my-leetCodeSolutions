# https://leetcode.com/problems/rotate-list/
from typing import Optional

from data_structures.list_node import ListNode


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def find_length_of_list(head: Optional[ListNode]):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    dummy = ListNode(next_node=head)
    for i in range(k):
        previous_node = dummy
        current_node = head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        current_node.next = dummy.next
        dummy.next = current_node
        previous_node.next = None
    return dummy.next
