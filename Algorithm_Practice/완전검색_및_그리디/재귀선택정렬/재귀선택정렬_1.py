def recurs_select_sort(given_list, starting):
    list_length = len(given_list)
    if starting >= list_length:
        return
    min_idx = starting
    for i in range(starting + 1, list_length):
        if given_list[i] < given_list[starting]:
            min_idx = i
    given_list[starting], given_list[min_idx] = given_list[min_idx], given_list[starting]
    recurs_select_sort(given_list, starting + 1)
