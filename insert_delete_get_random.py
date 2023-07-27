# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
import random


class RandomizedSet:

    def __init__(self):
        self.set_values = list()

    def insert(self, val: int) -> bool:
        if val not in self.set_values:
            self.set_values.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set_values:
            self.set_values.remove(val)
            return True
        return False

    def get_random(self) -> int:
        return random.choice(self.set_values)
