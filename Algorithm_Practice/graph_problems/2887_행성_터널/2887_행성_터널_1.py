# 행성 터널
# https://www.acmicpc.net/problem/2887
# 1144 1230 1330

def find_set(starting):
    if parent_list[starting] != starting:
        parent_list[starting] = find_set(parent_list[starting])
    return parent_list[starting]


def dist_planet(a, b):
    return min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


planets_cnt = int(input())
planets_list = [tuple(map(int, input().split() + [i])) for i in range(planets_cnt)]
print(planets_list)
parent_list = list(range(planets_cnt))
planets_dist_list = []
planets_list.sort(key=lambda x: x[0])
print(planets_list)
axis_planets = []
for i in range(1, planets_cnt):
    axis_planets.append((dist_planet(planets_list[i], planets_list[i - 1]), planets_list[i - 1][3], planets_list[i][3]))
planets_dist_list.append(axis_planets)
axis_planets = []
planets_list.sort(key=lambda x: x[1])
print(planets_list)
for i in range(1, planets_cnt):
    axis_planets.append((dist_planet(planets_list[i], planets_list[i - 1]), planets_list[i - 1][3], planets_list[i][3]))
planets_dist_list.append(axis_planets)
axis_planets = []
planets_list.sort(key=lambda x: x[2])
print(planets_list)
for i in range(1, planets_cnt):
    axis_planets.append((dist_planet(planets_list[i], planets_list[i - 1]), planets_list[i - 1][3], planets_list[i][3]))
planets_dist_list.append(axis_planets)
print(planets_dist_list)
tot_cost = 0
