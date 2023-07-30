# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
def candy(ratings: list[int]) -> int:
    candy_dist = [1] * (len(ratings))
    for index in range(len(ratings) - 1):
        if ratings[index] < ratings[index + 1]:
            candy_dist[index + 1] += 1
        elif ratings[index] > ratings[index + 1]:
            candy_dist[index] += 1
    return sum(candy_dist)
