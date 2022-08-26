# 1349 1358

import sys

sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    memory_number = input()
    prev_number = '0'
    change_count = 0
    for i in memory_number:
        if prev_number != i:
            change_count += 1
        prev_number = i
    print(f"#{test_count}", change_count)
