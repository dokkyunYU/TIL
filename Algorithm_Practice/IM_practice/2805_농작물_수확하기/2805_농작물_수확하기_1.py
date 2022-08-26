# 1313 1346
import sys

sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    n = int(input())
    farm_list = [list(map(int, input())) for _ in range(n)]
    result_sum = 0
    middle = n // 2
    for i in range(n):
        for j in range(n):
            if abs(i - middle) + abs(j - middle) <= middle:
                result_sum += farm_list[i][j]

    print(f"#{test_count}", result_sum)
