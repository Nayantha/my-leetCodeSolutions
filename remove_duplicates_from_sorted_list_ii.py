# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    ...
