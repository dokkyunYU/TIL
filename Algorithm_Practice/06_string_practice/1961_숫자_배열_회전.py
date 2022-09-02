# (i,j)

# 90도 회전

# (N-1-j,i)

# 180도 회전

# (N-1-i,N-1-j)

# 270도 회전

# (j,N-1-i)

# 0.30


# import sys

# sys.stdin = open("input.txt")

# T = int(input())

# for test_count in range(1, T + 1):
#     N = int(input())

#     the_list = [input().split() for _ in range(N)]

#     rotate_90_list = [[0] * N for _ in range(N)]
#     rotate_180_list = [[0] * N for _ in range(N)]
#     rotate_270_list = [[0] * N for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             rotate_90_list[i][j] = the_list[N - 1 - j][i]

#     for i in range(N):
#         for j in range(N):
#             rotate_180_list[i][j] = the_list[N - 1 - i][N - 1 - j]

#     for i in range(N):
#         for j in range(N):
#             rotate_270_list[i][j] = the_list[j][N - 1 - i]

#     print(f"#{test_count}")
#     for k in range(N):
#         print(
#             "".join(list(map(str, rotate_90_list[k]))),
#             "".join(list(map(str, rotate_180_list[k]))),
#             "".join(list(map(str, rotate_270_list[k]))),
#         )


T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')

    N = int(input())
    first_list = [list(map(int, input().split())) for _ in range(N)]
    #  270도 회전
    final_list = list(zip(*first_list))
    #  180도 회전
    thd_list = list(zip(*final_list))
    #  90도 회전
    # sec_list = list(zip(*thd_list))[::-1]

    for i in range(N):
        # print(*sec_list[i], sep='', end=' ')
        print(*thd_list[i], sep='', end=' ')
        print(*final_list[i], sep='', end=' ')
        print()
