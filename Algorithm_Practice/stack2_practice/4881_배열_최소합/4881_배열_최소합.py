# 1518

import sys

sys.stdin = open("input.txt")

def permutations(arr, depth, sum_now) -> list:
    global min_sum

    if sum_now >= min_sum:
        return

    if len(arr) == len(number_list):
        if sum_now < min_sum:
            min_sum = sum_now
        return

    for i in range(len(number_list)):
        if not used_list[i]:
            used_list[i] = True
            arr.append(i)
            sum_now += n_list[depth][i]

            permutations(arr, depth + 1, sum_now)

            sum_now -= n_list[depth][i]
            used_list[i] = False
            arr.pop()

    if not arr:
        return min_sum


for test_count in range(1, int(input()) + 1):
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(n)]
    number_list = list(range(n))
    used_list = [False] * n
    depth = 0
    the_arr = []
    min_sum = 100000000
    print(f"#{test_count}", permutations(the_arr, 0, 0))