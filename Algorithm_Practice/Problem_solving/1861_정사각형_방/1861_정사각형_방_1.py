# 정사각형 방
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc
# 1042 1405

import sys
sys.stdin = open("input.txt")


def route_search(x, y):
    start_num = room_number_list[x][y]
    now_num = start_num
    while True:
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < room_length and 0 <= ny < room_length and room_number_list[nx][ny] - now_num == 1:
                x, y = nx, ny
                now_num = room_number_list[nx][ny]
                break
        else:
            return now_num - start_num + 1


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for test_count in range(1, int(input()) + 1):
    room_length = int(input())
    room_number_list = [list(map(int, input().split()))
                        for _ in range(room_length)]
    max_distance = 0
    max_starting_num = float("inf")
    for i in range(room_length):
        for j in range(room_length):
            distance = route_search(i, j)
            if distance > max_distance:
                max_distance = distance
                max_starting_num = room_number_list[i][j]
            elif distance == max_distance and max_starting_num > room_number_list[i][j]:
                max_starting_num = room_number_list[i][j]
    print("#{} {} {}".format(test_count, max_starting_num, max_distance))
