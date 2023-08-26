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

    total_num_of_nodes = find_length_of_list(head)
    total_num_of_jumps = (total_num_of_nodes - k - 1) % total_num_of_nodes
    current_node = head
    for i in range(total_num_of_jumps):
        current_node = current_node.next
    new_head = current_node.next
    current_node.next = None
    current_node = new_head
    while current_node.next:
        current_node = current_node.next
    current_node.next = head
    return new_head
