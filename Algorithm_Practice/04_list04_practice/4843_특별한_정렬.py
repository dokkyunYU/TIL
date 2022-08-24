import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))
    result_list = []
    # N_list에 요소가 하나라도 들어있으면 계속 반복
    while N_list:
        # 리스트 내부의 값을 최대값으로 지정하면 값의 예상 범위를 몰라도 가능
        idx = 0
        maximum_value = N_list[0]
        # 현재 리스트에서 최대값을 찾아서 그 요소를 pop하여 result_list에 입력
        for i, j in enumerate(N_list):
            if maximum_value < j:
                maximum_value = j
                idx = i

        result_list += [N_list.pop(idx)]
        # 리스트 내부의 값을 최소값으로 지정하면 값의 예상 범위를 몰라도 가능
        idx = 0
        minimun_value = N_list[0]
        # 현재 리스트에서 최소값을 찾아서 그 요소를 pop하여 result_list에 입력
        for i, j in enumerate(N_list):
            if maximum_value > j:
                maximum_value = j
                idx = i

        result_list += [N_list.pop(idx)]

    print(f"#{test_count}", *result_list[:10])


# 0.40
