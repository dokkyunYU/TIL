# 2230 2340
import sys

sys.stdin = open("sample_input.txt", encoding="utf-8")

for test_count in range(1, int(input()) + 1):
    # 중복순열 문제...
    numbers_count = int(input())
    operator_count = list(map(int, input().split()))
    the_numbers = list(map(int, input().split()))
    print(the_numbers)
    # 2 1 6 2
    # 2 3 7 9 4 5 1 9 2 5 6 4
    # 중복순열을 어떻게 구현해야하나...
