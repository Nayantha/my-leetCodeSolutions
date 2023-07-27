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


class RandomizedSet2:
    def __init__(self):
        self.num_list = list()
        self.num_map = dict()

    def insert(self, val: int) -> bool:
        if val not in self.num_map:
            self.num_list.append(val)
            self.num_map[val] = self.num_list.index(val)
            # self.num_list.append(val)
            # self.num_map[val] = self.num_list.index(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.num_map:
            self.num_list[len(self.num_list)], self.num_list[self.num_map[val]] \
                = self.num_list[self.num_map[val]], self.num_list[
                len(self.num_list)]
            self.num_list.pop()
            self.num_map[
                self.num_list[self.num_map[val]]] = self.num_list.index(
                self.num_map[val])
            # self.num_map.
            return True
        return False
