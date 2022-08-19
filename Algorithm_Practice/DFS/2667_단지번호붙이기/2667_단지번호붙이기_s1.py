# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

# sys.setrecursionLimit(newLimit)

# 0925 1000

import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")


def dfs(x, y):
    visited[x][y] = True
    global total
    total += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
            dfs(nx, ny)


n = int(input())

board = [list(map(int, input())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * n for _ in range(n)]
result = []


for i in range(n):
    for j in range(n):
        # print(i, j, visited[i][j], board[i][j])
        if not visited[i][j] and board[i][j] == 1:
            total = 0
            dfs(i, j)
            result.append(total)

print(len(result), *sorted(result), sep='\n')
