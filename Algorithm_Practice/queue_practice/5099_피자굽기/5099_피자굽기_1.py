import sys
from collections import deque

sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    pizza_amount = [int(i) for i in input().split()]
    # 피자들의 인덱스를 미리 저장
    oven_queue = deque(list(range(n)))
    pizza_complete = []
    # 기다리고 있는 피자의 인덱스
    waiting_pizza = n
    # 큐가 전부 빌때까지
    while oven_queue:
        pizza_idx = oven_queue.popleft()
        pizza_amount[pizza_idx] //= 2
        # 만약 나눠서 0이 되었을때
        if pizza_amount[pizza_idx] == 0:
            # 기다리는 피자가 있다면 집어넣고 완성된 피자를 결과리스트에 추가 후 인덱스 1 증가
            if waiting_pizza < m:
                oven_queue.append(waiting_pizza)
                pizza_complete.append(pizza_idx)
                waiting_pizza += 1
            # 더이상 피자가 없다면 그냥 결과리스트에만 추가
            else:
                pizza_complete.append(pizza_idx)
        # 나눠서 0이 아니라면 그냥 다시 맨 뒤에 추가
        else:
            oven_queue.append(pizza_idx)
    print(f"#{test_count}", pizza_complete[-1] + 1)