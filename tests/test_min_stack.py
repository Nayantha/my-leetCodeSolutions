from min_stack import MinStack


class TestMinStack:
    def test_min_stack_01(self):
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        assert min_stack.get_min() == -3
        min_stack.pop()
        assert min_stack.top() == 0
        assert min_stack.get_min() == -2
