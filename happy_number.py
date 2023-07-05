# https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
def is_happy(n: int) -> bool:
    sum_of_square_seq = set()
    while n != 1:
        n = square_and_sum(n)
        if n in sum_of_square_seq:
            return False
        sum_of_square_seq.add(n)
    return True


def square_and_sum(n):
    return sum([pow(int(num), 2) for num in list(str(n))])
