def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0]*51 for _ in range(51)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1, x2 + 1):
            board[i][y1] += 1
            board[i][y2] += 1
        for j in range(y1, y2 + 1):
            board[x1][j] += 2
            board[x2][j] += 2
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                board[i][j] = 0
    
    dist = 0
    item_dist = 0
    dx, dy = 0, 0
    x, y  = characterX, characterY
    if board[x][y] == 3:
        if board[x+1][y] == 0:
            dx = -1
        else:
            dx = 1
    elif board[x][y] == 2:
        dy = 1
    else:
        dx = 1
    # print(*board,sep="\n")
    # print(rectangle, characterX, characterY, itemX, itemY)
    # print(x,y,dx,dy, board[x+dx][y+dy])
    while True:
        # print(x,y,dx,dy, board[x+dx][y+dy])
        while board[x][y] != 3:
            print(x,y)
            x += dx
            y += dy
            dist += 1
            if x == itemX and y == itemY:
                item_dist = dist
            if x == characterX and y == characterY:
                return item_dist if item_dist < dist - item_dist else dist - item_dist
        print(x,y,dx,dy, board[x+dx][y+dy])
        if dx:
            if board[x][y+1] == 2 or board[x][y+1] == 3:
                dy = 1
                dx = 0
            elif board[x][y-1] == 2 or board[x][y-1] == 3:
                dy = -1
                dx = 0
        elif dy:
            if board[x+1][y] == 1 or board[x+1][y] == 3:
                dx = 1
                dy = 0
            elif board[x-1][y] == 1 or board[x-1][y] == 3:
                dx = -1
                dy = 0
        x += dx
        y += dy
        dist += 1
        if x == itemX and y == itemY:
                item_dist = dist
        if x == characterX and y == characterY:
            return item_dist if item_dist < dist - item_dist else dist - item_dist

given = [[[[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8],
[[[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1],
[[[1, 1, 5, 7]], 1, 1, 4, 7],
[[[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10],
[[[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3]]
for h in range(5):
    print(solution(*given[h]))