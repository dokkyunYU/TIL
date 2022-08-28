# 경비원
# https://www.acmicpc.net/problem/2564
# 1732 1745 1756
import sys

sys.stdin = open("input.txt")

n, m = map(int, input().split())

shop_amount = int(input())

shop_location: list[list] = [list(map(int, input().split())) for _ in range(shop_amount)]

start_location: list = list(map(int, input().split()))

coordinate_list = []
for i in [start_location] + shop_location:
    if i[0] == 1:
        coordinate_list.append((i[1], 0))
    elif i[0] == 2:
        coordinate_list.append((i[1], m))
    elif i[0] == 3:
        coordinate_list.append((0, i[1]))
    else:
        coordinate_list.append((n, i[1]))
distance_sum = 0
for j in range(1, shop_amount + 1):
    if abs(coordinate_list[j][0] - coordinate_list[0][0]) == n:
        if m > coordinate_list[j][1] + coordinate_list[0][1]:
            distance_sum += coordinate_list[j][1] + coordinate_list[0][1] + n
        else:
            distance_sum += -coordinate_list[j][1] - coordinate_list[0][1] + n + 2 * m
    elif abs(coordinate_list[j][1] - coordinate_list[0][1]) == m:
        if n > coordinate_list[j][0] + coordinate_list[0][0]:
            distance_sum += coordinate_list[j][0] + coordinate_list[0][0] + m
        else:
            distance_sum += -coordinate_list[j][0] - coordinate_list[0][0] + m + 2 * n
    else:
        distance_sum += abs(coordinate_list[j][0] - coordinate_list[0][0])
        distance_sum += abs(coordinate_list[j][1] - coordinate_list[0][1])

print(distance_sum)
