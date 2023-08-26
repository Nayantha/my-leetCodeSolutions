from typing import Optional

from list_node import ListNode


def insert(head_node: Optional[ListNode], value: int):
    new_node = ListNode(val=value)
    if not head_node:
        head_node = new_node
    else:
        current_node = head_node
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    return head_node


def array_to_list(array: list[int], n: int = None):
    if not n:
        n = len(array)
    head: Optional[ListNode] = None
    for i in range(n - 1, -1, -1):
        head = insert(head, array[i])
    return head
