# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional

from data_structures.tree_node import TreeNode


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    node_stack = []
    current_node = root
    index_of_the_number = 0
    while node_stack or current_node:
        while current_node:
            node_stack.append(current_node)
            current_node = current_node.left
        current_node = node_stack.pop()
        index_of_the_number += 1
        if index_of_the_number == k:
            return current_node.val
        current_node = current_node.right
    return index_of_the_number

def kth_smallest_inorder(root: Optional[TreeNode], k: int) -> int:
    res = []

    def inorder(node: TreeNode) -> int:
        if node:
            inorder(node.left)
            if len(res) == k:
                return node.val
            res.append(node.val)
            inorder(node.right)

    return inorder(root)
