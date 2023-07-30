# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
def candy(ratings: list[int]) -> int:
    candy_dist = [1] * (len(ratings))
    for index in range(len(ratings) - 1):
        if ratings[index] < ratings[index + 1] and candy_dist[index] >= candy_dist[index + 1]:
            candy_dist[index + 1] += candy_dist[index]
        elif ratings[index] > ratings[index + 1] and candy_dist[index] <= candy_dist[index + 1]:
            candy_dist[index] += candy_dist[index]
    for index in range(len(ratings) - 1, 0, -1):
        if ratings[index] < ratings[index - 1] and candy_dist[index] > candy_dist[index - 1]:
            candy_dist[index - 1] += candy_dist[index]
        elif ratings[index] > ratings[index - 1] and candy_dist[index] <= candy_dist[index - 1]:
            candy_dist[index] += candy_dist[index]
    return sum(candy_dist)
