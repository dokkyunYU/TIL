import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    the_board = [[0] * 10 for _ in range(10)]
    N = int(input())
    # 보드 색칠
    for i in range(N):
        ix1, iy1, ix2, iy2, block_color = map(int, input().split())
        for x in range(ix1, ix2 + 1):
            for y in range(iy1, iy2 + 1):
                if the_board[x][y] == 0:
                    the_board[x][y] = block_color
                # 현재 입력하려는 색깔과 다른 어떤 무언가가 이미 있다면 무조건 보라색으로 변경
                # 여러 색깔들이 겹쳐지게 되어도 보라색 칸은 보라색을 유지
                elif the_board[x][y] != block_color:
                    the_board[x][y] = 3
    # 보라색 카운트
    purple_block_count = 0
    for j in range(10):
        for k in range(10):
            if the_board[j][k] == 3:
                purple_block_count += 1

    print(f"#{test_count} {purple_block_count}")

# 30
