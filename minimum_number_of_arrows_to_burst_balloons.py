def find_min_arrow_shots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    res = [points[0]]
    for start, end in points[1:]:
        last_end = res[-1][1]
        if start <= last_end:
            res[-1][1] = min(last_end, end)
            res[-1][0] = max(start, res[-1][0])
        else:
            res.append([start, end])
    return len(res)


def find_min_arrow_shots_with_limit(points: list[list[int]], limit: int = 2) -> int:
    """
    Burst limited number of balloons
    :param points: the points of X-axis the balloons spread across
    :param limit: the number of balloons an arrow is able to burst
    :return: the minimum arrows need to burst all balloons
    """
    points.sort(key=lambda x: x[1])
    res = [points[0] + [1]]
    for start, end in points[1:]:
        last_end = res[-1][1]
        if start <= last_end and res[-1][2] == limit - 1:
            res[-1][1] = min(last_end, end)
            res[-1][0] = max(start, res[-1][0])
            res[-1][2] += 1
        else:
            res.append([start, end, 1])
    return len(res)
