# https://leetcode.com/problems/min-stack/
class MinStack:
    """
    Extension of the stack data structure.
    Apart from the inherited methods, this class is able to return the minimum value reside in the stack.
    """

    def __init__(self):
        """
        Initialize the min stack.
        Stack keeps track of the values that pushes inside the stack.
        The other stack keeps track of the minimum values of each pop and push.
        """
        self.stack = []
        self.min_value_stack = []

    def push(self, val: int) -> None:
        """
        Push a value in to the stack.
        :param val: the value that need to be push in to the stack
        """
        self.stack.append(val)
        val = min(val, self.min_value_stack[-1] if self.min_value_stack else val)
        self.min_value_stack.append(val)

    def pop(self) -> None:
        """
        Remove the top value (the last values of the arrays).
        """
        self.stack.pop()
        self.min_value_stack.pop()

    def top(self) -> int:
        """
        Output the top value of the stack.
        In this implementation, the last value of the array stack.
        :return: Top value of the stack.
        """
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_value_stack[-1]
