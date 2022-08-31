# 0258
import sys

sys.stdin = open("input.txt")


def ordinary_bus(stations, start, end):
    stations[start] += 1
    stations[end] += 1
    for stop in range(start + 1, end):
        stations[stop] += 1
    return stations


def express_bus(stations, start, end):
    stations[start] += 1
    stations[end] += 1
    if start % 2 == 1:
        for stop in range(start + 1, end):
            if stop % 2 == 1:
                stations[stop] += 1
    else:
        for stop in range(start + 1, end):
            if stop % 2 == 0:
                stations[stop] += 1
    return stations


def super_express_bus(stations, start, end):
    stations[start] += 1
    stations[end] += 1
    if start % 2 == 1:
        for stop in range(start + 1, end):
            if stop % 3 == 0 and stop % 10 != 0:
                stations[stop] += 1
    else:
        for stop in range(start + 1, end):
            if stop % 4 == 0:
                stations[stop] += 1
    return stations


T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    bus_types = [list(map(int, input().split())) for _ in range(N)]

    all_stations = [0] * 1001

    for bus in bus_types:
        if bus[0] == 1:
            all_stations = ordinary_bus(all_stations, bus[1], bus[2])
        elif bus[0] == 2:
            all_stations = express_bus(all_stations, bus[1], bus[2])
        else:
            all_stations = super_express_bus(all_stations, bus[1], bus[2])

    max_value = 0
    for i in all_stations:
        if max_value < i:
            max_value = i

    print(f"#{test_count}", max_value)
