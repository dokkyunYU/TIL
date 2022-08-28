# 직사각형 네개의 합집합의 면적 구하기
# https://www.acmicpc.net/problem/2669
# 1406 1423
import sys

sys.stdin = open("input.txt")

board_list = [[0] * 101 for _ in range(101)]
result = 0
for _ in range(4):
    idx = list(map(int, input().split()))
    for i in range(idx[0], idx[2]):
        for j in range(idx[1], idx[3]):
            if board_list[i][j] != 1:
                board_list[i][j] = 1
                result += 1
print(result)
