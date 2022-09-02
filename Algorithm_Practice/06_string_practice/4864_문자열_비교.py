# 0955 0957

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    str1 = input()
    str2 = input()
    # str1이 str2에 존재하면 1 아니면 0 출력
    print(f"#{test_count}", 1 if str1 in str2 else 0)
