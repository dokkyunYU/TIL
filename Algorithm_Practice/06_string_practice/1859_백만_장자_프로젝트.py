# 0245 0337


import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    purchase_sum = 0
    price_list = list(map(int, input().split()))
    while len(price_list) > 1:
        max_price = max(price_list)
        max_idx = price_list.index(max_price)
        purchase_list = price_list[: max_idx + 1]
        purchase_sum += sum([max_price - i for i in purchase_list])
        # price_list = price_list[max_idx + 1 :]
        del price_list[: max_idx + 1]

    print(f"#{test_count}", purchase_sum)
