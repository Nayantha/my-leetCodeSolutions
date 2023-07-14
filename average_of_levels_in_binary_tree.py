# https://leetcode.com/problems/average-of-levels-in-binary-tree/solutions/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional, List

from binary_tree_inorder_traversal import TreeNode


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    d = {}

    def dfs(node=root, level=0):
        if not node: return
        level += 1
        d_v = d.get(level)
        if not d_v:
            d[level] = node.val
        else:
            d[level] = d_v + node.val
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs()
    return [v / k for k, v in d.items()]
