# https://leetcode.com/problems/product-of-array-except-self/
import numpy as np


def product_except_self(nums: list[int]) -> list[int]:
    product_list = []
    for index, current_num in enumerate(nums):
        nums_with_out_current_index_item = nums.copy()
        del nums_with_out_current_index_item[index]
        product_list.append(np.product(np.array(nums_with_out_current_index_item)))
    return product_list
