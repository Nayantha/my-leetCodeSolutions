# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
def candy(ratings: list[int]) -> int:
    total_num_of_ratings = len(ratings)
    candy_dist = [1] * total_num_of_ratings

    for i in range(1, total_num_of_ratings):
        if ratings[i] > ratings[i - 1]:
            candy_dist[i] = candy_dist[i - 1] + 1

    for i in range(total_num_of_ratings - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candy_dist[i] = max(candy_dist[i + 1] + 1, candy_dist[i])
    return sum(candy_dist)
