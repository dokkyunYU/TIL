import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))

    sorted_list = []

    while N_list:  # N_list가 빈 리스트가 될 때까지 루프
        min_value = N_list[0]
        pop_index = 0
        # 최소값을 찾아서 그 인덱스를 저장
        for i, j in enumerate(N_list):
            if min_value > j:
                min_value = j
                pop_index = i
        # 인덱스를 사용해 리스트 내의 요소를 pop
        sorted_list += [N_list.pop(pop_index)]

    print(f"#{test_count}", *sorted_list)
