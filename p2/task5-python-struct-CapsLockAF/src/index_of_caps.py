def index_of_caps(word):
    res = []
    for i, l in enumerate(word):
        l.isupper() and res.append(i)
    return res
