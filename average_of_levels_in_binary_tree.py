# https://leetcode.com/problems/average-of-levels-in-binary-tree/solutions/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional, List

from binary_tree_inorder_traversal import TreeNode


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    level_against_sum_dict = {}

    def traverse(node=root, level=0):
        if not node:
            return
        level += 1
        current_sum_of_level = level_against_sum_dict.get(level)
        if not current_sum_of_level:
            level_against_sum_dict[level] = node.val
        else:
            level_against_sum_dict[level] = current_sum_of_level + node.val
        traverse(node.left, level + 1)
        traverse(node.right, level + 1)

    traverse()
    list = list()
    for k, v in level_against_sum_dict.items():
        if k == 0:
            list.append(v)
        elif k == 1:
            list.append(v)
        else:
            list.append(k / v)
    return list
