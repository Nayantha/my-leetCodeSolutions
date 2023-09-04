# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
from data_structures.tree_node import TreeNode


def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return TreeNode()
    if root == p or root == q:
        return root
    l = lowest_common_ancestor(root.left, p, q)
    r = lowest_common_ancestor(root.right, p, q)
    if l and r:
        return root
    else:
        return l or r
