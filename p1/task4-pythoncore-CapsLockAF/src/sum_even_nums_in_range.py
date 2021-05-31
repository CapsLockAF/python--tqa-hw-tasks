def sum_even_nums_in_range(start, stop):
    # Type your code
    t = range(start, stop + 1)
    c = filter(lambda x: x % 2 == 0, t)
    return sum(c)


print(sum_even_nums_in_range(63, 97))