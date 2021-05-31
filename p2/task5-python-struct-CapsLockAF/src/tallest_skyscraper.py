def tallest_skyscraper(sky_list):
    w = len(sky_list[0])
    h = len(sky_list)
    l = []
    for c in range(w):
        count = 0
        for r in range(h):
            if sky_list[r][c]:
                count += 1
        l.append(count)
    return max(l)
