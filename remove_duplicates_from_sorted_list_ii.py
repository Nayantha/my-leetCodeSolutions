# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
from typing import Optional

from list_node import ListNode


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(next_node=head)
    previous_node = dummy
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            previous_node.next = head.next
        else:
            previous_node = previous_node.next
        head = head.next
    return dummy.next
