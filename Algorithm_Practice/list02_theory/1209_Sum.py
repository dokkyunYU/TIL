# 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

import sys

sys.stdin = open("input.txt")

T = 10

for test_count in range(1, T + 1):

    N_list = []

    N = input()

    for _ in range(100):
        N_list.append(list(map(int, input().split())))

    highest_value = 0

    local_sum = 0

    # 행 최대값 구하기
    for ix in range(100):
        local_sum = 0
        for iy in range(100):
            local_sum += N_list[ix][iy]
        if local_sum > highest_value:
            highest_value = local_sum

    local_sum = 0
    # 열 최대값 구하기
    for jy in range(100):
        local_sum = 0
        for jx in range(100):
            local_sum += N_list[jx][jy]
        if local_sum > highest_value:
            highest_value = local_sum

    local_sum = 0
    # 대각선 \ 최대값 구하기
    for k in range(100):
        local_sum += N_list[k][k]
    if local_sum > highest_value:
        highest_value = local_sum

    local_sum = 0
    # 대각선 / 최대값 구하기
    for h in range(100):
        local_sum += N_list[h][99 - h]
    if local_sum > highest_value:
        highest_value = local_sum

    print(f"#{test_count} {highest_value}")
