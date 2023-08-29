# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import Optional

from data_structures.tree_node import TreeNode


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    root: Optional[TreeNode] = None
    for i in preorder:
        new_node = TreeNode(val=i, left=inorder[:inorder.index(i)], right=inorder[inorder.index(i) + 1:])
        if not root:
            root = new_node
    return root
