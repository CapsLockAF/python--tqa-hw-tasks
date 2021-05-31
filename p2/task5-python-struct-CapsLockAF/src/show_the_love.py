def show_the_love(share_list):
    sm_i = share_list.index(min(share_list))
    res = list(share_list)

    for i, n in enumerate(share_list):
        if n > share_list[sm_i]:
            x = (n / 100 * 25)
            res[i] = n - x
            res[sm_i] += x

    return res
