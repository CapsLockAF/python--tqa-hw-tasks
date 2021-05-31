def pops(pop_list):
    n = pop_list[len(pop_list)//2]
    for i in range(n):
        pop_list[n - 1 - i] = n - i - 1
        pop_list[n + 1 + i] = n - 1 - i
    return pop_list
