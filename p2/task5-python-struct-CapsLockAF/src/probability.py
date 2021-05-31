def probability(numbers_list, number):
    c = len(tuple(filter(lambda x: x >= number, numbers_list)))
    return round(c * 100 / len(numbers_list), 1)

