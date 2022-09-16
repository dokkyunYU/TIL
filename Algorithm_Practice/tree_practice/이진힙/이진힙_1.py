# 이진힙
# 1424 1446

import sys
sys.stdin = open("sample_input.txt")


def heap_push(item):
    # 받은 아이템을 우선 힙 리스트에 넣는다
    min_heap.append(item)
    # 현재 집어넣은 아이템의 인덱스를 계산
    idx_now = len(min_heap) - 1
    # 부모노드의 인덱스를 계산한다
    parent_idx = idx_now // 2
    # 최상위 노드 즉 루트노드까지 갈 동안
    while parent_idx >= 1:
        # 만약 부모노드의 값이 자식노드의 값보다 크다면
        if min_heap[parent_idx] > min_heap[idx_now]:
            # 두 값을 바꾼다
            min_heap[parent_idx], min_heap[idx_now] = min_heap[idx_now], min_heap[parent_idx]
            # 현재 노드의 인덱스를 부모것으로 바꾼다
            idx_now = parent_idx
            # 부모 노드의 인덱스를 다시 현재 노드의 부모로 바꾼다
            parent_idx = idx_now // 2
        # 만약 한번이라도 부모노드의 값이 자식노드보다 크지 않은 경우
        else:
            # 반복문을 종료한다
            break


for test_count in range(1, int(input()) + 1):
    numbers = int(input())
    min_heap = [0]
    for i in tuple(map(int, input().split())):
        heap_push(i)
    sum_idx = (len(min_heap) - 1) // 2
    result_sum = 0
    # 가장 뒤 인덱스의 노드로부터 부모로 올라오며 노드의 값을 더한다
    while sum_idx >= 1:
        result_sum += min_heap[sum_idx]
        sum_idx //= 2
    print(f"#{test_count}", result_sum)
