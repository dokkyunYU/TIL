def advance(row, col, drow, dcol, mode):
    global dead_zone
    if room_list[row][col] == 6:
        return 1
    if not (0 <= row < n and 0 <= col < m):
        return 1
    if advance(row + drow, col + dcol, drow, dcol, mode):
        if mode == 1 and room_list[row][col] <= 0:
            if room_list[row][col] == 0:
                dead_zone -= 1
            room_list[row][col] -= 1
        elif mode == 0 and room_list[row][col] < 0:
            if room_list[row][col] == -1:
                dead_zone += 1
            room_list[row][col] += 1


class cam:
    def __init__(self, camera):
        a, b, c, d = camera
        self.camera = [a, b, c, d]

    def rotate(self):
        return [self.camera.pop()] + self.camera


cam1 = [0, 1, 0, 0]
cam2 = [0, 1, 0, 1]
cam3 = [1, 1, 0, 0]
cam4 = [1, 1, 0, 1]
cam5 = [1, 1, 1, 1]
dir_list = [0, cam1, cam2, cam3, cam4, cam5]
n, m = map(int, input().split())
room_list = [list(map(int, input().split())) for _ in range(n)]
dead_zone = n * m
cam_list = []
rotate_cnt = []
for i in range(n):
    for j in range(m):
        if room_list[i][j] in [1, 2, 3, 4, 5]:
            cam_list.append((room_list[i][j], i, j))
            rotate_cnt.append(0)
for x, y, z in cam_list:
    a, b, c, d = dir_list[x]
    if a:
        advance(y, z, -1, 0, 1)
    if b:
        advance(y, z, 0, 1, 1)
    if c:
        advance(y, z, 1, 0, 1)
    if d:
        advance(y, z, 0, -1, 1)

while rotate_cnt[-1] < 4:
    for x, y, z in cam_list:
        a, b, c, d = dir_list[x]
        if a:
            advance(y, z, -1, 0, 1)
        if b:
            advance(y, z, 0, 1, 1)
        if c:
            advance(y, z, 1, 0, 1)
        if d:
            advance(y, z, 0, -1, 1)
    rotate_cnt[0] += 1
