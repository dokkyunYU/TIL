import sys

sys.stdin = open("input.txt")

test_count = 10

# 건물의 앞뒤 2개의 건물들을 세기 위한 리스트
need_to_check = [-2, -1, 1, 2]

for i in range(1, test_count + 1):
    ground_length = int(input())
    buildings_height = list(map(int, input().split()))
    good_sight_houses = 0
    for j in range(2, ground_length - 2):
        highest_building = 0
        # j번째 건물의 앞뒤 2개씩 건물중 가장 높은 건물
        for k in need_to_check:
            if buildings_height[j + k] > highest_building:
                highest_building = buildings_height[j + k]
        # 앞뒤 2개의 건물중 가장 높은 건물과 j번째 건물과의 차이 == 전망권이 좋은 세대
        if buildings_height[j] - highest_building > 0:
            good_sight_houses += buildings_height[j] - highest_building

    print(f"#{i} {good_sight_houses}")
