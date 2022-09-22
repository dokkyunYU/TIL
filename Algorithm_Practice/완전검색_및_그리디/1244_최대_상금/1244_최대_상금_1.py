# 최대 상금
# 3 + 1624 1740
import sys
sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    numbers_string, exchange_count = input().split()
    exchange_count = int(exchange_count)
    numbers_list = list(map(int, numbers_string))
    numbers_list_2 = list(map(int, numbers_string))
    exchange_list = []
    numbers_length = len(numbers_list)
    for i in range(numbers_length):
        max_value = numbers_list[i]
        max_idx = i
        for j in range(i + 1, numbers_length):
            if numbers_list[j] >= max_value:
                max_value = numbers_list[j]
                max_idx = j
        if i != max_idx:
            numbers_list[i], numbers_list[max_idx] = numbers_list[max_idx], numbers_list[i]
            exchange_list.append([i, max_idx])
            exchange_count -= 1
            if exchange_count == 0:
                break
    else:
        for _ in range(exchange_count):
            numbers_list[-1], numbers_list[-2] = numbers_list[-2], numbers_list[-1]
    max_money = int("".join(map(str, numbers_list)))
    numbers_list = list(map(int, numbers_string))
    for k in range(len(exchange_list)):
        for t in range(k + 1, len(exchange_list)):
            exchange_list[k][1], exchange_list[t][1] = exchange_list[t][1], exchange_list[k][1]
            for h in exchange_list:
                numbers_list[h[0]], numbers_list[h[1]] = numbers_list[h[1]], numbers_list[h[0]]
            max_money2 = int("".join(map(str, numbers_list)))
            numbers_list = list(map(int, numbers_string))
            if max_money < max_money2:
                max_money = max_money2
    print("#{} {}".format(test_count, max_money))
