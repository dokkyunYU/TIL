# 베이비진 게임
# 1528 1620

import sys
sys.stdin = open("sample_input.txt")


def is_tri_run(given_list):
    given_list.sort()
    for i in range(len(given_list) - 2):
        if given_list[i] == given_list[i + 1] == given_list[i + 2]:
            return True
    given_set_list = sorted(list(set(given_list)))
    for j in range(len(given_set_list) - 2):
        if given_set_list[j] + 2 == given_set_list[j + 1] + 1 == given_set_list[j + 2]:
            return True


for test_count in range(1, int(input()) + 1):
    card_list = list(map(int, input().split()))
    first_card_list = card_list[0::2]
    second_card_list = card_list[1::2]
    result = 0
    for i in range(3, 7):
        if is_tri_run(first_card_list[:i]):
            result = 1
            break
        if is_tri_run(second_card_list[:i]):
            result = 2
            break
    print(f"#{test_count}", result)
