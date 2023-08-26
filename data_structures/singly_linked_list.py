from typing import Optional

from list_node import ListNode


def insert(head_node: Optional[ListNode], value: int):
    new_node = ListNode(val=value)
    if not head_node:
        head_node = new_node
        return
    current_node = head_node
    while current_node.next:
        current_node = current_node.next
    current_node.next = new_node
