# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import List, Optional

from binary_tree_inorder_traversal import TreeNode


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    # get middle element that is the root

    def get_middle_element(num_list: List[int]):
        if not num_list:
            return
        middle_element_index = len(num_list) // 2
        node = TreeNode(val=num_list[middle_element_index])
        node.left = get_middle_element(num_list[:middle_element_index])
        node.right = get_middle_element(num_list[middle_element_index + 1:])
        return node

    return get_middle_element(nums)
