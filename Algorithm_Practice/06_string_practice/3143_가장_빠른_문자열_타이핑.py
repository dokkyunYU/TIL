# 0914 0919

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    A, B = input().split()

    A = A.replace(B, " ")

    # 공백으로 치환후 숫자 카운트
    print(f"#{test_count}", len(A))
