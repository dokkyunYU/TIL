n = int(input())
n_card_queue = list(range(1, n + 1))
result_list = []
while len(n_card_queue) > 1:
    result_list.append(n_card_queue.pop(0))
    if len(n_card_queue) <= 1:
        result_list.append(n_card_queue.pop())
        break
    n_card_queue.append(n_card_queue.pop(0))
print(*result_list)