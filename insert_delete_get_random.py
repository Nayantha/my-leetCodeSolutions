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
            index_of_value_to_be_removed = self.num_map[val]
            last_value_of_list = self.num_list[-1]
            self.num_list[index_of_value_to_be_removed] = last_value_of_list
            # replace the last value with val if the set need to catch that value in future
            # self.num_list[-1] = val
            self.num_list.pop()
            self.num_map[last_value_of_list] = index_of_value_to_be_removed
            del self.num_map[val]
            return True
        return False
