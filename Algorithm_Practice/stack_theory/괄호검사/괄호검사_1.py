# 2054 2059

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    the_list = input()
    count_for_test = 0
    for i in the_list:
        if i == "(":
            count_for_test += 1
        elif i == ")":
            count_for_test -= 1

    print(f"#{test_count}", 1 if count_for_test == 0 else -1)
