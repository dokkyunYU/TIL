# 1400 1555
import sys
from collections import deque

sys.stdin = open("input.txt")


def bfs(queue, depth) -> int:
    global route_queue
    # 넘겨받은 큐가 비었다면 더이상 갈곳이 없으므로 바로 리턴한다
    if not route_queue[-1] == 3:
        return
    else:
        # 큐의 가장 처음 좌표를 받아서 스타트로 삼는다
        x, y = queue.popleft()
        # 상하좌우를 탐색하며 갈 수 있는(1이 아닌) 좌표를 큐에 추가한다
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and maze_list[nx][ny] != 1
                and not visited[nx][ny]
            ):
                # 만약 3을 만난다면 글로벌 변수를 현재 깊이로 대입하고 함수를 종료한다
                if maze_list[nx][ny] == 3:
                    destination_depth = depth
                    return
                # 갈 수 있는 좌표를 큐에 추가하고 방문한 것으로 한다
                visited[nx][ny] = True
                route_queue.append((nx, ny))
        # 만들어진 큐와 함께 깊이를 +1하여 재귀호출한다
        bfs(route_queue, depth + 1)
        # 재귀호출된 함수가 종료되면 본 함수도 종료한다
    return


def recursive_bfs(queue, depth) -> int:
    global route_queue


for test_count in range(1, int(input()) + 1):
    n = int(input())
    maze_list = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start_point = []
    destination_depth = 0
    for i in range(n):
        for j in range(n):
            if maze_list[i][j] == 2:
                # 스타트지점 한개만 들어있는 큐를 생성
                route_queue = deque([[i, j]])
    # 큐와 깊이를 입력하여 함수를 호출한다
    bfs(start_point, 0)
    print(f"#{test_count}", destination_depth)
