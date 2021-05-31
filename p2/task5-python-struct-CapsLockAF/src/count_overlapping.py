def count_overlapping(list_intervals, point):
    res2 = len([x for x in list_intervals if x[1] >= point >= x[0]])
    return res2
