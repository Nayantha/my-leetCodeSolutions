class ListNode:
    """
    ListNode keep track of the value and what node comes next.
    """

    def __init__(self, val=0, next_node=None):
        """
        Initialize ListNode.
        :param val: Value of the Node.
        :param next_node: What node comes next.
        """
        self.val = val
        self.next = next_node
