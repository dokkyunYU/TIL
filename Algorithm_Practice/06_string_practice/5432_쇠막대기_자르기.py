# 1116 0236


import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    steel_and_laser = input()
    steel_and_laser = steel_and_laser.replace("()", "1")
    steel_bar_count = 0
    laser_count = 0
    cutted_steel_bar_count = 0
    for i in steel_and_laser:

        if i == "(":
            steel_bar_count += 1

        elif i == ")":
            cutted_steel_bar_count += 1
            steel_bar_count -= 1

        elif i == "1":
            cutted_steel_bar_count += steel_bar_count

    print(f"#{test_count}", cutted_steel_bar_count)
