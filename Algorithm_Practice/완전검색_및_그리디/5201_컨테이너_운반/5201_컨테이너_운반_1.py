# 컨테이너 운반
# 1318 1331

import sys
sys.stdin = open("sample_input.txt")

for test_count in range(1, int(input()) + 1):
    items_count, trucks_count = map(int, input().split())
    items_list = list(map(int, input().split()))
    trucks_list = list(map(int, input().split()))
    items_list.sort()
    trucks_list.sort(reverse=True)
    loaded_weight = 0
    while items_list:
        item_now = items_list.pop()
        for i in range(trucks_count):
            if trucks_list[i] >= item_now:
                trucks_list[i] = 0
                loaded_weight += item_now
                break
    print(f"#{test_count}", loaded_weight)