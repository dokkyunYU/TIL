# 감시
# https://www.acmicpc.net/problem/15683
# 1629

# 시계방향 : 상 우 하 좌
cam1 = [1, 0, 0, 0]
cam2 = [1, 0, 1, 0]
cam3 = [1, 1, 0, 0]
cam4 = [1, 1, 0, 1]

class cam:
    room_list = []
    dead_zone = 0
    def __init__(self, look_dir):
        self.look_dir = look_dir
    

    def rooms(self, room):
        cam.room_list = room

    def looks(self):
        



# row, col = map(int, input().split())
# room_list = [list(map(int, input().split())) for _ in range(row)]
# dead_zone = row * col
# for i in range(row):
#     for j in range(col):
#         if room_list[i][j]:
#             dead_zone -= 1
#             if room_list[i][j] == 1:
#                 pass

