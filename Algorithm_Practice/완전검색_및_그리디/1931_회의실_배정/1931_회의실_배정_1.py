# 회의실 배정
# https://www.acmicpc.net/problem/1931
# 1419 1520

import sys
sys.stdin = open("input.txt")

meeting_count = int(input())
meeting_info = [tuple(map(int, input().split())) for _ in range(meeting_count)]
meeting_info.sort(key=lambda x: (x[1], x[0]))
end = meeting_info[0][1]
schedule_count = 0
for i in meeting_info:
    if i[0] >= end:
        end = i[1]
        schedule_count += 1
print(schedule_count)