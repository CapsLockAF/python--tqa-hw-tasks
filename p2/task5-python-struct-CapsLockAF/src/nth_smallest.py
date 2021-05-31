def nth_smallest(list_numbers, ind_num):
    nums = []
    if ind_num == len(list_numbers):
        return list_numbers[-1]
    elif ind_num < len(list_numbers):
        for i in list_numbers[:ind_num]:
            i < list_numbers[ind_num] and nums.append(i)
        if ind_num == 1 and len(nums) == 0:
            return ind_num
        elif len(nums):
            return max(nums)
        else:
            return list_numbers[ind_num]
    else:
        return None
