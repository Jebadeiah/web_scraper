def find_my_list(all_lsts, my_list):
    for indy, lst in enumerate(all_lsts):
        if lst is my_list:
            return indy
    return None
