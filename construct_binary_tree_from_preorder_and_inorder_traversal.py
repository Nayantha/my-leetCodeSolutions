# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import Optional

from data_structures.tree_node import TreeNode


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])
    return root


def create_new_node(inorder: list[int]) -> Optional[TreeNode]:
    if not inorder:
        return None
    middle_index = len(inorder) // 2
    node = TreeNode(val=inorder[middle_index])
    node.left = create_new_node(inorder[:middle_index])
    node.right = create_new_node(inorder[middle_index + 1:])
    return node
