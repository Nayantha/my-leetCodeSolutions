# https://leetcode.com/problems/average-of-levels-in-binary-tree/solutions/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional, List

from binary_tree_inorder_traversal import TreeNode


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    same_level_node_sum = dict()
    def traverse(node=root, level=0):
        if not root:
            return
        level += 1
        dict_value = same_level_node_sum.get(level)
        if not dict_value:
            same_level_node_sum[level] = node.val
        else:
            same_level_node_sum[level] += node.val
        traverse(node.left, level)
        traverse(node.right, level)
    traverse()
    return [value / key for key, value in same_level_node_sum.items()]
