# 0.35

# 영준이는 당근 크기 선별기를 이용해 수확한 순서대로 당근의 크기를 기록하였다. 이 당근 선별기에는 특별한 기능이 있는데 연속으로 당근의 크기가 커진 경우 그 개수를 알려준다.
# 당근의 크기가 수확한 순서로 주어질 때, 선별기가 알려준 연속으로 커지는 당근의 갯수는 최대 얼마인지 확인하기 위한 프로그램을 만드시오. 연속으로 커지지않는 경우 구간의 최소 길이는 1이다.
# N개의 당근을 수확하며, 당근의 크기 C는 1부터 10까지의 정수로 정해진다.
# 5<=N<=1000, 1<=C<=10

# 입력
# 첫 줄에 테스트케이스의 개수 T, 다음 줄 부터 테스트케이스별로 첫 줄에 당근 개수 N, 다음 줄 당근의 크기 C를 의미하는 N개의 정수가 주어진다.


import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))
    maximum_order_counting = 1
    order_counting = set()

    for i in range(len(N_list) - 1):
        if N_list[i + 1] - N_list[i] == 1:
            order_counting.add(i)
            order_counting.add(i + 1)
        else:
            if maximum_order_counting < len(order_counting):
                maximum_order_counting = len(order_counting)
            order_counting = set()

    if maximum_order_counting < len(order_counting):
        maximum_order_counting = len(order_counting)

    print(f"#{test_count} {maximum_order_counting}")
