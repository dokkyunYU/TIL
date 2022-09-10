n, m, width, height = map(int, input().split())

red_dot = []
blue_dot = []
for _ in range(n):
    red_dot.append(list(map(int, input().split())))
for _ in range(m):
    blue_dot.append(list(map(int, input().split())))
x_range = [float("inf"), 0]
y_range = [float("inf"), 0]

for i, j in red_dot + blue_dot:
    if i < x_range[0]:
        x_range[0] = i
    if j < y_range[0]:
        y_range[0] = j
    if i > x_range[1]:
        x_range[1] = i
    if j > y_range[1]:
        y_range[1] = j
max_value = 0
max_xy = []
x_range[0] -= width
y_range[0] -= height
for x in range(x_range[0], x_range[1] + 1):
    for y in range(y_range[0], y_range[1] + 1):
        red_count = 0
        blue_count = 0
        for t in red_dot:
            if x <= t[0] <= x + width and y <= t[1] <= y + height:
                red_count += 1
        for k in blue_dot:
            if x <= k[0] < x + width and y <= k[1] <= y + height:
                blue_count += 1
        if max_value < abs(red_count - blue_count):
            max_value = abs(red_count - blue_count)
            max_xy = [x, y]
print(max_value)
print(*max_xy)
