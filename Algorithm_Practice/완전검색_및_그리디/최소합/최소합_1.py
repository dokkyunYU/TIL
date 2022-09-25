# 최소합
# 1525 1555


def route_finder(row, col, route_sum):
    global min_route_sum
    route_sum += numbers_list[row][col]
    if route_sum > min_route_sum:
        return
    if row == length_n - 1 and col == length_n - 1 and route_sum < min_route_sum:
        min_route_sum = route_sum
    if row < length_n - 1:
        route_finder(row + 1, col, route_sum)
    if col < length_n - 1:
        route_finder(row, col + 1, route_sum)


for test_count in range(1, int(input()) + 1):
    length_n = int(input())
    numbers_list = [list(map(int, input().split())) for _ in range(length_n)]
    min_route_sum = float("inf")
    route_finder(0, 0, 0)
    print("#{} {}".format(test_count, min_route_sum))
