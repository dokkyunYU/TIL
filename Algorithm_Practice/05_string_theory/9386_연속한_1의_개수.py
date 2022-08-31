import sys

sys.stdin = open("input.txt", encoding="UTF-8")

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, [i for i in input()]))
    number1_maximum = 0
    for i in range(1, len(N_list)):
        N_list[i] = N_list[i - 1] * N_list[i] + N_list[i]

    for j in N_list:
        if number1_maximum < j:
            number1_maximum = j
    print(f"#{test_count} {number1_maximum}")

# 0.15
