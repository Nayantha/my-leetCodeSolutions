# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
class RandomizedSet:

    def __init__(self):
        self.randomized_set = set()

    def insert(self, val: int) -> bool:
        if val in self.randomized_set:
            return False
        self.randomized_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        ...

    def get_random(self) -> int:
        ...
