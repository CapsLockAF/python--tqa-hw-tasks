def len_longest_chain(chain_pairs):
    s1 = sorted(chain_pairs)
    count = 1
    for i, el in enumerate(s1[1:]):
        if el[0] > s1[i - 1][1]:
            count += 1
    return count

