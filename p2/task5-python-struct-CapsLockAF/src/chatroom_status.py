def chatroom_status(users_list):
    num = len(users_list)
    return not num and f"no one online" or \
        num == 1 and f"{users_list[0]} online" or \
        num == 2 and f"{users_list[0]} and {users_list[1]} online" or \
        num > 2 and f"{users_list[0]}, {users_list[1]} and {num - 2} " \
                       f"more online"
