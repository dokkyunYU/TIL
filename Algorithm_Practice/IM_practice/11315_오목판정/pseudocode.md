# 개념

어떻게 대각선 및 가로 세로까지 다 검토하면서 연산을 줄일 수 있을까

이중리스트를 순회하다가 o를 만나면 

우, 우하, 하, 좌하를 검색하면 된다(반대편 방향들은 위에서부터 좌로 검색을 시작하므로 생각할 필요 없다)


# pseudocode
```
def omok(start_x, start_y):
  result = 0
  for k in range(4):
    x, y = start_x, start_y
    for t in range(4):
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



dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]


```