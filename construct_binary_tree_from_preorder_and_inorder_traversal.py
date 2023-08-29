# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import Optional

from data_structures.tree_node import TreeNode


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    root = TreeNode(val=preorder[0])
    index_of_root_value_in_inorder_list = inorder.index(preorder[0])
    root.left = create_new_node(inorder[:index_of_root_value_in_inorder_list])
    root.right = create_new_node(inorder[index_of_root_value_in_inorder_list + 1:])
    return root


def create_new_node(inorder: list[int]) -> Optional[TreeNode]:
    if not inorder:
        return None
    middle_index = len(inorder) // 2
    node = TreeNode(val=inorder[middle_index])
    node.left = create_new_node(inorder[:middle_index])
    node.right = create_new_node(inorder[middle_index + 1:])
    return node
