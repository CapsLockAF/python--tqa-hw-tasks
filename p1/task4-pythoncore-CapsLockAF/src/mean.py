def mean(number):
    s = str(number)
    return int(sum((int(x) for x in s)) / len(s))
