class ListNode:
    """
    ListNode keep track of the value and what node comes next.
    """

    def __init__(self, val=0, next=None):
        """
        Initialize ListNode.
        :param val: Value of the Node.
        :param next: What node comes next.
        """
        self.val = val
        self.next = next
