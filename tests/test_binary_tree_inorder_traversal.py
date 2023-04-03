import pytest

from binary_tree_inorder_traversal import Solution, TreeNode
class TestSolution:
    @pytest.mark.parametrize("root, expected", [
        ([1, None, 2, 3], [1, 3, 2])
        # ([], []),
        # ([1], [1])
    ])
    def test_inorder_traversal(self, root, expected):
        treeNodes = [TreeNode(val=num) for num in root]
        treeNodes[0].left = treeNodes[1]
        treeNodes[0].right = treeNodes[2]
        treeNodes[2].left = treeNodes[3]
        sol = Solution()
        assert sol.inorderTraversal(treeNodes[0]) == expected
