def priority_sort(unsort_lst, pri_set):
    s1 = sorted(set(pri_set).intersection(unsort_lst))
    s2 = sorted(set(unsort_lst).difference(s1))
    lst = [i for i in unsort_lst if i in pri_set]
    return sorted(lst) + s2
