# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
import random


class RandomizedSet:

    def __init__(self):
        self.randomized_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.randomized_set:
            self.randomized_set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randomized_set:
            self.randomized_set.remove(val)
            return True
        return False

    def get_random(self) -> int:
        return random.choice(list(self.randomized_set))
