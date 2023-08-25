# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
from typing import Optional

from list_node import ListNode


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(next_node=head)
    previous_node, current_node = dummy, head
    while current_node:
        if current_node.val == current_node.next.next.val:
            while current_node.val == current_node.next.next.val:
                current_node = current_node.next
            current_node = current_node.next
            previous_node.next = current_node
        previous_node = current_node
        current_node = current_node.next
    return dummy.next
