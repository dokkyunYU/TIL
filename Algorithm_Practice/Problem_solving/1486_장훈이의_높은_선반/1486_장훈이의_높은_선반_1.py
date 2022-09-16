# 장훈이의 높은 선반
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw
# 1015 1035

import sys
sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    clerks_count, tower_height = map(int, input().split())
    clerks_tall = list(map(int, input().split()))
    min_tall_difference = float("inf")
    for i in range(1 << clerks_count, 1 << clerks_count + 1):
        tall_sum = 0
        for j in range(0, clerks_count):
            if i & (1 << j):
                tall_sum += clerks_tall[j]
        if tall_sum >= tower_height and min_tall_difference > tall_sum - tower_height:
            min_tall_difference = tall_sum - tower_height
            if min_tall_difference == 0:
                break
    print("#%d %d" % (test_count, min_tall_difference))
