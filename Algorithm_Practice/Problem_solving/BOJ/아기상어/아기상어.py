import sys
from collections import deque

sys.stdin = open("input.txt")

drow = [-1, 0, 0, 1]
dcol = [0, -1, 1, 0]

def bfs(x, y, size=2, eat=0, time=0):
    global alltime, visit
    # print(x, y, size, time)
    queue = deque([(x, y)])
    is_there = 0
    select_list = []
    while queue:
        row, col = queue.popleft()
        if 0 < board[row][col] < size:
            # print(board[row][col], row, col)
            if not is_there:
                # print(1)
                is_there = visit[row][col]
                select_list.append((row, col))
            elif visit[row][col] == is_there:
                select_list.append((row, col))
            else:
                board[row][col] = 0
                visit = [[0 for _ in range(n)] for _ in range(n)]
                # visit[row][col] = 1
                row, col = sorted(select_list, key=lambda x: (x[0], x[1]))[0]
                eat += 1
                if size == eat:
                    size += 1
                    eat = 0
                bfs(row, col, size, eat, time + visit[row][col])

        for i in range(4):
            if 0 <= row + drow[i] < n and 0 <= col + dcol[i] < n and not visit[row+drow[i]][col+dcol[i]] and board[row+drow[i]][col+dcol[i]] <= size:
                queue.append((row+drow[i], col+dcol[i]))
                visit[row+drow[i]][col+dcol[i]] = visit[row][col] + 1
    # print(2)
    if not queue:
        if alltime < time:
            alltime = time
        return


for test_cnt in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    alltime = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                visit[i][j] = 1
                board[i][j] = 0
                bfs(i, j)
    print(alltime)