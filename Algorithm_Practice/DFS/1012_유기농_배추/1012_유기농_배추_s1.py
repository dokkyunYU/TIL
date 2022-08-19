# 유기농 배추
# https://www.acmicpc.net/problem/1012

# 1000 1050

import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")


def dfs(x, y):
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and baechu[nx][ny] == 1:
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for test_count in range(1, t + 1):

    n, m, k = map(int, input().split())
    worm_count = 0
    baechu: list[list[int]] = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        idx_x, idx_y = map(int, input().split())
        # print(idx_x, idx_y)
        baechu[idx_x][idx_y] = 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and baechu[i][j] == 1:
                worm_count += 1
                dfs(i, j)

    print(worm_count)
