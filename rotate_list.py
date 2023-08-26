# https://leetcode.com/problems/rotate-list/
from typing import Optional

from data_structures.list_node import ListNode


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return head
    total_num_of_nodes, tail = 1, head
    while tail.next:
        total_num_of_nodes += 1
        tail = tail.next

    k = k % total_num_of_nodes
    if k == 0:
        return head

    current_node = head
    for i in range(total_num_of_nodes - k - 1):
        current_node = current_node.next

    new_head = current_node.next
    current_node.next = None

    tail.next = head
    return new_head
