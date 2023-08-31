# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    cur, nxt = root, root.left if root else None
    while cur and nxt:
        cur.left.next = cur.right
        if cur.next:
            if cur.next.left:
                cur.right.next = cur.next.left
            else:
                cur.right.next = cur.next.right
        cur = cur.next
        if not cur:
            cur = nxt
            nxt = cur.left
    return root
