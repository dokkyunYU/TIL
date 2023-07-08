def dfs(depth, length_sum):
    global length_min
    if depth == core_count:
        if length_sum < length_min:
            length_min = length_sum
        return
    for each_core in core_location:
        x, y = each_core
        for k1 in range(0, x):
            if core_location[k1][y] != 0:
                break
        else:
            dfs(depth + 1, length_sum + (x - 1))
        for k2 in range(0, y):
            if core_location[x][k2] != 0:
                break
            else:
                dfs(depth + 1, length_sum + (y - 1))
        for k3 in range(x + 1, square_length):
            if core_location[k3][y] != 0:
                break
        else:
            dfs(depth + 1, length_sum + (square_length - x - 1))
        for k3 in range(x + 1, square_length):
            if core_location[k3][y] != 0:
                break
        else:
            dfs(depth + 1, length_sum + (square_length - y - 1))




T = int(input())
for test_case in range(1, T + 1):
    square_length = int(input())
    square_list = [list(map(int, input().split())) for _ in range(square_length)]
    core_location = []
    core_count = 0
    length_min = 10**6
    for i in range(square_length):
        for j in range(square_length):
            if square_list[i][j] == 1:
                if i == 0 or j == 0 or i == square_length - 1 or j == square_length - 1:
                    continue
                else:
                    core_location.append((i, j))
                    core_count += 1
    dfs(0, 0)
    # 표준출력(화면)으로 답안을 출력합니다.
    print("#%d" % test_case)
