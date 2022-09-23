# 화물 도크
# 1341 1416

import sys
sys.stdin = open("sample_input.txt")

for test_count in range(1, int(input()) + 1):
    trucks_count = int(input())
    trucks_list = [tuple(map(int, input().split())) for _ in range(trucks_count)]
    trucks_list.sort(key=lambda x: x[1] - x[0])
    work_count = 0
    work_schedule = set()
    for i in trucks_list:
        if not(work_schedule & set(range(i[0], i[1]))):
            work_schedule = work_schedule | set(range(i[0], i[1]))
            work_count += 1
    print(f"#{test_count}", work_count)
