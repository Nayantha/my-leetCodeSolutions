# https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
def is_happy(n: int) -> bool:
    if n == 1:
        return True
    if len(str(n)) == 1:
        return False
    return is_happy(sum([pow(int(num), 2) for num in list(str(n))]))
