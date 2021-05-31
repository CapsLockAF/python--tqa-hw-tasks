def identical_filter(words):
    return [x for x in words if len(set(x)) < 2]
