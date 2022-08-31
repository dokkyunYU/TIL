# 0225 0257

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N, M = map(int, input().split())
    the_picture = [list(map(int, input().split())) for _ in range(N)]
    maximum_value = 0
    for i in range(N):
        row_sum = 0
        for j in range(M):
            if the_picture[i][j] == 0 and row_sum > maximum_value:
                maximum_value = row_sum

            row_sum = the_picture[i][j] * row_sum + the_picture[i][j]

        if row_sum > maximum_value:
            maximum_value = row_sum

    for m in range(M):
        col_sum = 0
        for h in range(N):
            if the_picture[h][m] == 0 and col_sum > maximum_value:
                maximum_value = col_sum

            col_sum = the_picture[h][m] * col_sum + the_picture[h][m]

        if col_sum > maximum_value:
            maximum_value = col_sum

    print(f"#{test_count}", maximum_value)
