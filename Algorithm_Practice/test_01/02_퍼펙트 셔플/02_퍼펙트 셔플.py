# 02_퍼펙트 셔플
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW
# 0.20

import sys

sys.stdin = open("input.txt")

t = int(input())

for test_count in range(1, t + 1):
    n = int(input())
    card_list = list(input().split())
    first_card_list = card_list[: (n + 1) // 2]
    second_card_list = card_list[(n + 1) // 2 :]
    result_card_list = []
    while second_card_list:
        result_card_list.append(first_card_list.pop(0))
        result_card_list.append(second_card_list.pop(0))
    print(f"#{test_count}", *(result_card_list + first_card_list))
