# 1115 1309
import sys

sys.stdin = open("sample_input.txt")

def omok(start_x, start_y):
  result = 0
  for k in range(4):
    x, y = start_x, start_y
    for _ in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if omok_list[nx][ny] != "o":
          break
        x = nx
        y = ny
      else:
        break
    else:
      result += 1
  return result


for test_count in range(1, int(input()) + 1):
    n = int(input())
    # ".o"
    dx = [1, 1, 0, -1]
    dy = [0, 1, 1, 1]
    is_omok_there = 0
    omok_list = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if omok_list[i][j] == "o":
                is_omok_there = omok(i, j)
                if is_omok_there:
                    break
        if is_omok_there:
            break

    print(f"#{test_count}", "YES" if is_omok_there != 0 else "NO")





