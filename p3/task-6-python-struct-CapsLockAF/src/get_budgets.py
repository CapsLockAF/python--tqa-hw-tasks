def get_budgets(lst_budgets):
    res = 0
    for i in lst_budgets:
        res += i.get("budget")
    return res
