import sys

sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    room_length = int(input())
    room_list = [list(map(int, input().split())) for _ in range(room_length)]

    person_coordinate_list = []
    stair_coordinate_list = []
    for i in range(room_length):
        for j in range(room_length):
            if room_list[i][j] == 1:
                person_coordinate_list.append((i, j))
            elif room_list[i][j] > 1:
                stair_coordinate_list.append((i, j, room_list[i][j]))

    people_distance_list = []
    some_list = []
    for k in range(len(person_coordinate_list)):
        some_list.append(k)
        some_list.append(
            abs(person_coordinate_list[k][0] - stair_coordinate_list[0][0])
            + abs(person_coordinate_list[k][1] - stair_coordinate_list[0][1])
        )
        some_list.append(
            abs(person_coordinate_list[k][0] - stair_coordinate_list[1][0])
            + abs(person_coordinate_list[k][1] - stair_coordinate_list[1][1])
        )
        people_distance_list.append(some_list)
        some_list = []
    print(people_distance_list)
    stair1_list = sorted(people_distance_list, key=lambda x: x[1])
    stair2_list = sorted(people_distance_list, key=lambda y: y[2])
    stair1_queue = []
    stair2_queue = []
    time = 0
    while True:
        time += 1
        if time == stair1_list[0][1]:
            stair1_queue.append(stair1_list[0][1].pop(0))
        if time == stair2_list[0][2]:
            stair2_queue.append(stair2_list[0][1].pop(0))
