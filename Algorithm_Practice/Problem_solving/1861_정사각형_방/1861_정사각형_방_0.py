dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move(start, n, x, y, step):
    for _ in range(4):
        if 0 <= x + dx[_] < N and 0 <= y + dy[_] < N and matrix[x + dx[_]][y + dy[_]] == n + 1:
            return move(start, matrix[x + dx[_]][y + dy[_]], x + dx[_], y + dy[_], step + 1)
    return start, step


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    moves = []

    for i in range(N):
        for j in range(N):
            moves.append(move(matrix[i][j], matrix[i][j], i, j, 1))

    ans = max(moves, key=lambda x: (x[1], -x[0]))

    print(f'#{tc + 1} {ans[0]} {ans[1]}')
