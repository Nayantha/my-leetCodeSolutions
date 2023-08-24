# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional

from add_two_numbers import ListNode


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = head
    total_nodes = 0
    while dummy:
        total_nodes += 1
        dummy = dummy.next
    index_of_node_to_remove = total_nodes - n
    dummy = head
    for i in range(index_of_node_to_remove - 1):
        dummy = dummy.next
    dummy.next = dummy.next.next
    return head
