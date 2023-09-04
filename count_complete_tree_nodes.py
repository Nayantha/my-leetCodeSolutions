# https://leetcode.com/problems/count-complete-tree-nodes/
from typing import Optional

from data_structures.tree_node import TreeNode


def count_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_tree, right_tree = root, root
    left_height, right_height = 0, 0
    while left_tree:
        left_height += 1
        left_tree = left_tree.left
    while right_tree:
        right_height += 1
        right_tree = right_tree.right
    if left_height == right_height:
        return pow(2, right_height)
    return 1 + count_nodes(root.left) + count_nodes(root.right)
