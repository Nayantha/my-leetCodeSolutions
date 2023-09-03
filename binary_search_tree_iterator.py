# https://leetcode.com/problems/binary-search-tree-iterator/
from typing import Optional

from data_structures.tree_node import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root.val)
            root = root.left

    def next(self) -> int:
        ...

    def hasNext(self) -> bool:
        return self.stack != []
