# 0952 0955


import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    str1 = input()
    str2 = input()
    max_str_count = 0
    # str1을 순회하며 str2에 들어있는 숫자를 세고, 그 숫자중 가장 큰 수를 출력
    for i in str1:
        if max_str_count < str2.count(i):
            max_str_count = str2.count(i)
    print(f"#{test_count}", max_str_count)
