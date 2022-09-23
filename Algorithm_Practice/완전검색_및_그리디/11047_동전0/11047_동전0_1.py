# 동전 0
# https://www.acmicpc.net/problem/11047
# 0922 0933

coins_count, target_value = map(int, input().split())
coins = [int(input()) for _ in range(coins_count)]
result_list = []
for i in range(len(coins) - 1, -1, -1):
    result_list.append(target_value // coins[i])
    target_value = target_value % coins[i]
print(sum(result_list))
