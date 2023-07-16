# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import List, Optional

from binary_tree_inorder_traversal import TreeNode


def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
    def initialize_tree_node(val: int) -> TreeNode:
        return TreeNode(val=val)

    def assign_node_to_parent(parent: TreeNode, new_node: TreeNode):
        if new_node.val > parent.val:
            if not parent.right:
                parent.right = new_node
            else:
                assign_node_to_parent(parent.right, new_node)
        else:
            if not parent.left:
                parent.left = new_node
            else:
                assign_node_to_parent(parent.left, new_node)

    root = None
    for num in nums:
        node = initialize_tree_node(num)
        if not node:
            root = node
            continue

    return root
