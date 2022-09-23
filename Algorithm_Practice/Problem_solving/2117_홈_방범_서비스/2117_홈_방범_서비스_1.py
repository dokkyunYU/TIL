# 홈 방범 서비스
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu
# 1142 1222

import sys

sys.stdin = open("sample_input.txt")


def dist_mapping(x, y):
    for a in range(city_size):
        for b in range(city_size):
            house_dist_list[a][b].append(abs(a - x) + abs(b - y))


for test_count in range(1, int(input()) + 1):
    city_size, fee = map(int, input().split())
    city_list = [list(map(int, input().split())) for _ in range(city_size)]
    house_dist_list = [[[] for _ in range(city_size)] for _ in range(city_size)]
    house_count_list = []
    for i in range(city_size):
        for j in range(city_size):
            if city_list[i][j] == 1:
                dist_mapping(i, j)
    for n in range(city_size):
        for m in range(city_size):
            for dist in set(house_dist_list[n][m]):
                house_count = 0
                for each_dist in house_dist_list[n][m]:
                    if each_dist <= dist:
                        house_count += 1
                if house_count * fee >= (dist + 1) ** 2 + dist ** 2:
                    house_count_list.append(house_count)
    print("#{} {}".format(test_count, max(house_count_list)))
