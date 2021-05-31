def sum_primes(list_numbers):
    res = 0

    def check_prime(x):
        for y in range(2, x):
            if x % y == 0:
                return False
        return True

    for i in list_numbers:
        if i > 1 and check_prime(i):
            res += i

    return 0 if list_numbers and not res else res or None
