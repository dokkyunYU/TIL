# 섬의 개수
# https://www.acmicpc.net/problem/4963

# 1050 1059

import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")


def dfs(x, y):
    visited[x][y] = True
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if (
            0 <= nx < h
            and 0 <= ny < w
            and not visited[nx][ny]
            and land_and_sea[nx][ny] == 1
        ):
            dfs(nx, ny)


dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
# t = int(input())

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    island_count = 0
    land_and_sea: list[list[int]] = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and land_and_sea[i][j] == 1:
                island_count += 1
                dfs(i, j)

    print(island_count)
