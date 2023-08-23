# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional

from add_two_numbers import ListNode


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    Reverse the list from position left to position right and switch the pointers of position (left-1) to position right
    and (right+1) to position left.
    :param head: The head of the singly-linked list.
    :param left: The starting index of the sub-list that needed to be reversed.
    :param right: The ending index of the sub-list that needed to be reversed.
    :return: The head of the new list; that is the list containing reversed sub-list
    """
    dummy_node = ListNode(0, head)
    left_previous_pointer, curr = dummy_node, head
    for i in range(left - 1):
        left_previous_pointer, curr = curr, curr.next
    prev = None
    for i in range(right - left + 1):
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node
    # now curr is the node at position (right + 1), prev is pointing at the node at position right
    left_previous_pointer.next.next = curr
    left_previous_pointer.next = prev
    return dummy_node.next
