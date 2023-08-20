# https://leetcode.com/problems/min-stack/
class MinStack:
    min_val: int | None = None

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.min_val or self.min_val > val:
            self.min_val = val
        self.stack[-1] = val

    def pop(self) -> None:
        ...

    def top(self) -> int:
        ...

    def get_min(self) -> int:
        ...
