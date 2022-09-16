# 탈주범 검거
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq
# 1636

import sys
sys.stdin = open("sample_input.txt")

def criminal_location(start_row, start_col):
    global place_count
    search_queue.append((start_row, start_col))
    visited_list[start_row][start_col] = 1
    while search_queue:
        row_now, col_now = search_queue.pop(0)
        place_count += 1
        for i in range(4):
            if (0 <= col_now + dcol[i] < width
                and 0 <= row_now + drow[i] < height
                and pipe_list[row_now][col_now] in now_opened[i]
                and pipe_list[row_now + drow[i]][col_now + dcol[i]] in next_opened[i]
                    and not visited_list):
                search_queue.append((row_now + drow[i], col_now + dcol[i]))
                visited_list[row_now + drow[i]][col_now + dcol[i]] = visited_list[row_now][col_now] + 1


right_opened = [1, 3, 4, 5]
left_opened = [1, 3, 6, 7]
up_opened = [1, 2, 4, 7]
down_opened = [1, 2, 5, 6]
now_opened = [right_opened, left_opened, up_opened, down_opened]
next_opened = [left_opened, right_opened, down_opened, up_opened]
dcol = [1, -1, 0, 0]
drow = [0, 0, -1, 1]
for test_count in range(1, int(input()) + 1):
    height, width, hole_row, hole_col, time_flowed = map(int, input().split())
    pipe_list = [[list(map(int, input().split()))] for _ in range(height)]
    visited_list = [[0 for _ in range(width)] for _ in range(height)]
    search_queue = []
    place_count = 0
    criminal_location(hole_row, hole_col)
    print(place_count)