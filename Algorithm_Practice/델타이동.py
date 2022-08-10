import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    N_list = []
    for _ in range(N):
        N_list.append(list(map(int, input().split())))
    absolute_sum = 0
    for ix in range(N):
        for iy in range(N):
            # 델타 검색은 결국 덧셈을 해서 변수를 하나 더 생성하고, 이후 if문 조건 검토 횟수도 별차이 없길래
            # 아래와 같이 넣어봤습니다.
            if ix > 0:
                absolute_sum += abs(N_list[ix][iy] - N_list[ix - 1][iy])
            if ix < N - 1:
                absolute_sum += abs(N_list[ix][iy] - N_list[ix + 1][iy])
            if iy > 0:
                absolute_sum += abs(N_list[ix][iy] - N_list[ix][iy - 1])
            if iy < N - 1:
                absolute_sum += abs(N_list[ix][iy] - N_list[ix][iy + 1])

    print(f"#{test_count} {absolute_sum}")


##### 여기서부턴 원래의 델타이동 #####


tc = int(input())

for r in range(tc):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]  #####여기까지는 입력 그대로 받기

    dx = [0, 1, 0, -1]  ## 우 하 좌 상
    dy = [1, 0, -1, 0]

    result = 0  ## 최종 결과를 담을 변수

    for n in range(N):
        for m in range(N):
            for k in range(4):
                if (
                    0 <= n + dx[k] <= N - 1 and 0 <= m + dy[k] <= N - 1
                ):  ## 더하기 전에 먼저 상하좌우 해당 인덱스가 존재하는지 조사하기.
                    result += abs(arr[n + dx[k]][m + dy[k]] - arr[n][m])

    print(f"#{r + 1} {result}")
