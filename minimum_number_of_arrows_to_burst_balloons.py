def find_min_arrow_shots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[0])
    res = [points[0] + [1]]
    for start, end in points[1:]:
        last_end = res[-1][1]
        if start <= last_end and res[-1][2] == 1:
            res[-1][1] = max(last_end, end)
            res[-1][2] += 1
        else:
            res.append([start, end, 1])
    return len(res)
