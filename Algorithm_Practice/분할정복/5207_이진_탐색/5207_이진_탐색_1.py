# 이진탐색
# 1457 1730

import sys
sys.stdin = open("sample_input.txt")

for test_count in range(1, int(input()) + 1):
    A_count, B_count = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    A_list.sort()
    bin_tree = [0]
    numbers_count = 0
    for i in B_list:
        left = 0
        right = A_count - 1
        middle = (left+right)//2
        now_num = i - A_list[middle]
        prev_num = -now_num
        if now_num == 0:
            numbers_count += 1
            continue
        while now_num * prev_num < 0:
            if i - A_list[middle] > 0:
                left = middle + 1
            elif i - A_list[middle] < 0:
                right = middle - 1
            middle = (left + right) // 2
            prev_num = now_num
            now_num = i - A_list[middle]
        if now_num != 0:
            continue
        numbers_count += 1
    print(f"#{test_count}", numbers_count)