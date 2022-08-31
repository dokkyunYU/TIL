# 0328


import sys
from pprint import pprint

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    modified_N_list = [[0] * (N + 2 * M) for _ in range(N + 2 * M)]
    for i in range(N):
        for j in range(N):
            modified_N_list[i + M][j + M] = N_list[i][j]
    maximum_flies_sum = 0
    for k in range(N):
        for h in range(N):
            cross_flies_sum = 0
            diagonal_flies_sum = 0
            for t in range(1, M):

                diagonal_flies_sum += modified_N_list[(k + M) + t][(h + M) + t]
                diagonal_flies_sum += modified_N_list[(k + M) - t][(h + M) + t]
                diagonal_flies_sum += modified_N_list[(k + M) - t][(h + M) - t]
                diagonal_flies_sum += modified_N_list[(k + M) + t][(h + M) - t]

                cross_flies_sum += modified_N_list[(k + M) + t][(h + M)]
                cross_flies_sum += modified_N_list[(k + M) - t][(h + M)]
                cross_flies_sum += modified_N_list[(k + M)][(h + M) + t]
                cross_flies_sum += modified_N_list[(k + M)][(h + M) - t]

            cross_flies_sum += modified_N_list[(k + M)][(h + M)]
            diagonal_flies_sum += modified_N_list[(k + M)][(h + M)]

            if diagonal_flies_sum > maximum_flies_sum:
                maximum_flies_sum = diagonal_flies_sum
            if cross_flies_sum > maximum_flies_sum:
                maximum_flies_sum = cross_flies_sum
    print(f"#{test_count}", maximum_flies_sum)
