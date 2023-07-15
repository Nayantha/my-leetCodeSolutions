# https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

from binary_tree_inorder_traversal import TreeNode


def get_minimum_difference(root: Optional[TreeNode]) -> int:
    bts_node_values = []

    def traverse(node=root):
        if not node:
            return
        bts_node_values.append(node.val)
        traverse(node.left)
        traverse(node.right)
    traverse()
    node_node_complement = set()
    for i, val1 in enumerate(bts_node_values[:-1]):
        for val2 in bts_node_values[i + 1:]:
            node_node_complement.add(abs(val1 - val2))
    return min(node_node_complement)
