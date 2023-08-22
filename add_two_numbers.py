# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result_list = l1
    remainder = 0
    l1_str = ""
    while l1:
        l1_str += str(l1.val)
        l1 = l1.next
    l2_str = ""
    while l2:
        l2_str += str(l2.val)
        l2 = l2.next
    add = str(int(l1_str[::-1]) + int(l2_str[::-1]))[::-1]
    result_node_list = [ListNode(int(x)) for x in add]
    result = result_node_list[0]
    cur = result
    for i in result_node_list[1:]:
        cur.next = i
        cur = cur.next
    return result
