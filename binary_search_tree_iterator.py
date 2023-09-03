# https://leetcode.com/problems/binary-search-tree-iterator/
from typing import Optional

from data_structures.tree_node import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        ...

    def next(self) -> int:
        ...

    def hasNext(self) -> bool:
        ...
