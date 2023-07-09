from typing import Optional

# https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return ListNode()
    if not list2:
        return list1
    if not list1:
        return list2
    ref = merged_list = ListNode()
    while list1 or list2:
        if list1.val == list2.val:
            ref.next = list1
            list1 = list1.next
            ref = ref.next

            ref.next = list2
            list2 = list2.next

        if list1.val < list2.val:
            ref = list1
            list1 = list1.next
        else:
            ref = list2
            list2 = list2.next
        ref = ref.next

    if not list1:
        merged_list.next = list2
    if not list2:
        merged_list.next = list1

    return merged_list.next
