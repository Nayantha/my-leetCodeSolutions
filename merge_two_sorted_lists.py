from typing import Optional

# https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    data_list = []
    while list1:
        data_list.append(list1.val)
        list1 = list1.next
    while list2:
        data_list.append(list2.val)
        list2 = list2.next
    list_nodes = [ListNode(val=data) for data in sorted(data_list)]
    for i, list_node in enumerate(list_nodes[:-1]):
        list_node.next = list_nodes[i + 1]
    return list_nodes[0]
