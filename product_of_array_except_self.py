# https://leetcode.com/problems/product-of-array-except-self/
import numpy as np


def product_except_self(nums: list[int]) -> list[int]:
    product_list = []
    for index, current_num in enumerate(nums):
        product_list.append(
            np.product(
                np.array(
                    [num for num in nums if nums.index(num) != index and num != current_num]
                )
            )
        )
    return product_list
