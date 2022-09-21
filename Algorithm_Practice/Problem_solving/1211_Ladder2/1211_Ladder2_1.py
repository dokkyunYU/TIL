import sys

sys.stdin = open('input.txt', encoding='utf-8')

for test_count in range(1, 11):
    input()
    ladder_list = [list(map(int, input().split())) for _ in range(100)]
    route_location = []
    for i in range(100):
        if ladder_list[0][i]:
            route_location.append(i)
    total_distance_sum = float("inf")
    minimum_x_location = 0
    for j in range(len(route_location)):
        distance_sum = 0
        x_idx = j
        x_location = route_location[x_idx]
        for y_location in range(100):
            if x_idx > 0:
                if ladder_list[y_location][x_location - 1]:
                    distance_sum += abs(route_location[x_idx - 1] - route_location[x_idx]) - 1
                    x_idx -= 1
                    x_location = route_location[x_idx]
                    continue
            if x_idx < len(route_location) - 1:
                if ladder_list[y_location][x_location + 1]:
                    distance_sum += abs(route_location[x_idx + 1] - route_location[x_idx]) - 1
                    x_idx += 1
                    x_location = route_location[x_idx]
        if total_distance_sum > distance_sum:
            total_distance_sum = distance_sum
            minimum_x_location = route_location[j]
    print(f"#{test_count}", minimum_x_location)