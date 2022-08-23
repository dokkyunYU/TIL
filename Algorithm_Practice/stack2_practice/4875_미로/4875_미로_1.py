# 1415 1508

import sys

sys.stdin = open("input.txt")

def maze_runner(x, y, given_list: list) -> int:
    route_stack = []
    while True:
        # 델타이동으로 주변 탐색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 만약 갈 수 있다면 그곳으로 이동하고 원래 있던 곳을 1로 바꿈
            if 0 <= nx < n and 0 <= ny < n and given_list[nx][ny] != 1:
                # 도착점이라면 True 반환
                if given_list[nx][ny] == 3:
                    return True
                # 델타이동한 방향을 스택에 저장
                route_stack.append(k)
                given_list[x][y] = 1
                x = nx
                y = ny
                break
        # 모든 델타이동 방향에 갈 수 있는 곳이 없다면 for문은 정상종료되고 else문 실행
        else:
            # 스택이 비어서 더이상 돌아갈 곳이 없다면 False 반환
            if not route_stack:
                return False
            # 돌아갈 수 있다면 현재 위치를 1로 바꾸고 스택에 저장된 델타이동을 거꾸로 수행
            given_list[x][y] = 1
            go_back = route_stack.pop()
            x = x - dx[go_back]
            y = y - dy[go_back]



for test_count in range(1, int(input()) + 1):
    n = int(input())
    maze_list = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze_list[i][j] == 2:
                start_x, start_y = i, j
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    can_go_out = maze_runner(start_x, start_y, maze_list)
    print(f"#{test_count}", int(can_go_out))