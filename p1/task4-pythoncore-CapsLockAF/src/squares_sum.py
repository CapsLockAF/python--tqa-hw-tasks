def squares_sum(n):
    # Type your code
    count = 1
    res = 0
    while count <= n:
        res += count**2
        count += 1
    return res
