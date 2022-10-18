import sys

sys.stdin = open("input.txt")

# 시계방향 : 상 우 하 좌
cam1 = [0, 1, 0, 0]
cam2 = [0, 1, 0, 1]
cam3 = [1, 1, 0, 0]
cam4 = [1, 1, 0, 1]
cam5 = [1, 1, 1, 1]
dir_list = [0, cam1, cam2, cam3, cam4, cam5]


class cam:
    room_list = []
    safe_zone = 0
    row = 0
    col = 0

    def __init__(self, look_dir, x, y):
        self.look_dir = look_dir
        self.x = x
        self.y = y

    def rotate(self, rotate_cnt):
        if rotate_cnt == 0:
            i, j = self.x, self.y
            for k, d in enumerate(self.look_dir):
                while 0 <= i < cam.row and 0 <= j < cam.col:
                    if i == self.x and j == self.y:
                        continue
                    elif cam.room_list[i][j] == 6:
                        break
                    elif cam.room_list[i][j] < 0:
                        if cam.room_list[i][j] == -1:
                            cam.safe_zone += 1
                        cam.room_list[i][j] += 1
                    if k == 0:
                        i -= d
                    elif k == 1:
                        j += d
                    elif k == 2:
                        i += d
                    else:
                        j -= d
            self.look_dir = self.look_dir.pop() + self.look_dir
            return rotate_cnt

    def observe(self):
        i, j = self.x, self.y
        for k, d in enumerate(self.look_dir):
            while 0 <= i < cam.row and 0 <= j < cam.col:
                if i == self.x and j == self.y:
                    continue
                elif cam.room_list[i][j] == 6:
                    break
                elif cam.room_list[i][j] <= 0:
                    if cam.room_list[i][j] == 0:
                        cam.safe_zone -= 1
                    cam.room_list[i][j] -= 1
                if k == 0:
                    i -= d
                elif k == 1:
                    j += d
                elif k == 2:
                    i += d
                else:
                    j -= d


cam.row, cam.col = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(cam.row)]
cam.room_list = room
cam_list = []
for i in range(cam.row):
    for j in range(cam.col):
        if room[i][j] in [1, 2, 3, 4, 5]:
            cam_list.append(cam(dir_list[room[i][j]], i, j))
rotate_cnt = [0 for _ in range(len(cam_list))]
while True:
    rotate_cnt[0] += 1
    for i in range(6):
        if rotate_cnt[i] // 4:
            rotate_cnt[i + 1] += 1
            rotate_cnt[i] %= 4
