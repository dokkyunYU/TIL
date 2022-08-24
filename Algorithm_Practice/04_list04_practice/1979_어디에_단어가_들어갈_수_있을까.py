import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N, K = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    letters_count = 0
    for i in range(N):
        # 행 합과 열 합을 초기화
        row_sum = 0
        column_sum = 0
        for j in range(N):
            # 어느쪽이든 0이 나온다면 총합에 산입하기 전에 현재 행 합 혹은 열 합이 K인지 검토
            if N_list[i][j] == 0 and row_sum == K:
                letters_count += 1
            if N_list[j][i] == 0 and column_sum == K:
                letters_count += 1
            # 총합 = 총합 * 리스트에서 도출된 수 + 리스트에서 도출된 수
            # 이렇게 하면, 리스트에서 1이 도출될때마다 1씩 숫자가 늘어나지만, 0이 나오는 순간 0으로 초기화된다.
            # 행과 열을 순차적으로 따라가며 0과 0사이에 1이 몇개 있는지가 총합sum으로 표현된다.
            row_sum = row_sum * N_list[i][j] + N_list[i][j]
            column_sum = column_sum * N_list[j][i] + N_list[j][i]
        # 0으로 끝나지 않는 경우 sum == K를 검토하는 과정이 일어나지 않는다.
        # 그런 경우를 위해 한번 더 검토과정을 준비한다.
        if row_sum == K:
            letters_count += 1
        if column_sum == K:
            letters_count += 1

    print(f"#{test_count}", letters_count)
