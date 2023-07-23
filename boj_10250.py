# https://www.acmicpc.net/problem/10250

for case in range(int(input())):
    floor, wide, customer = map(int, input().split())
    customer -= 1
    room_num = str(customer // floor + 1)
    print(str(customer % floor + 1) + (room_num if len(room_num) > 1 else "0" + room_num))
