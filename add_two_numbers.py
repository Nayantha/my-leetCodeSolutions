# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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


def add_two_numbers_ii(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    carry = 0
    while l1 or l2 or carry:
        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0
        addition = num1 + num2 + carry
        carry = addition // 10
        cur.next = ListNode(val=addition % 10)
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
