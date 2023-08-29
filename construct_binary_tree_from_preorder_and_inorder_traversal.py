# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import Optional

from data_structures.tree_node import TreeNode


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    root: Optional[TreeNode] = None
    for i in preorder:
        new_node = create_new_node(i, inorder)
        if not root:
            root = new_node
    return root


def create_new_node(i: int, inorder: list[int]) -> Optional[TreeNode]:
    if i not in inorder:
        return None
    new_node: Optional[TreeNode] = TreeNode(val=i, left=inorder[:inorder.index(i)],
                                            right=inorder[inorder.index(i) + 1:])
    left_tree_value_list = inorder[:inorder.index(i)]
    if not left_tree_value_list:
        return None
    left_tree_value = left_tree_value_list[len(left_tree_value_list) // 2]
    new_node.left = create_new_node(left_tree_value, left_tree_value_list)
    right_tree_value_list = inorder[inorder.index(i) + 1:]
    if not right_tree_value_list:
        return None
    right_tree_value = right_tree_value_list[len(right_tree_value_list) // 2]
    new_node.right = create_new_node(right_tree_value, right_tree_value_list)
    return new_node
