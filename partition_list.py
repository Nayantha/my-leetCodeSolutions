# https://leetcode.com/problems/partition-list/
from typing import Optional

from data_structures.list_node import ListNode


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """
    Given the head of a linked list and a value x,
    partition it such that all nodes less than x come before nodes greater than or equal to x.
    :param head: The head / first node of the linked list.
    :param x: The value to partition the linked list by.
    :return: Head of the partitioned linked list.
    """
    left, right = ListNode(), ListNode()
    left_tail, right_tail = left, right
    while head:
        if head.val < x:
            left_tail.next = head
            left_tail = left_tail.next
        else:
            right_tail = head
            right_tail = right_tail.next
        head = head.next
    left_tail.next = right.next
    right_tail.next = None
    return left.next


def partition_ii(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    dummy = ListNode(next_node=head)
    current_node = head.next if head.next else head
    left_list = head
    while current_node.next:
        if current_node.next.val < x:
            node_to_remove: ListNode = current_node.next
            current_node.next = node_to_remove.next
            node_to_remove.next = left_list.next
            left_list.next = node_to_remove
        current_node = current_node.next
    return dummy.next
