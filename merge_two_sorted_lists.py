from typing import Optional

#https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultList = ListNode()
        ref = resultList
        if list1.next is None or list2.next is None:
            return []
        if list1.next is None:
            return list2
        if list2.next is None:
            return list1
        
        if list1.val <= list2.val:
            resultList = list1
            list1 = list1.next
        else:
            resultList = list2
            list2 = list2.next
        
        ref = resultList
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                ref.next = list1
                list1 = list1.next
            else:
                ref.next = list2
                list2 = list2.next
            ref = ref.next
        if list1 is None:
            ref.next = list2
        
        if list2 is None:
            ref.next = list1
        
        return resultList
        