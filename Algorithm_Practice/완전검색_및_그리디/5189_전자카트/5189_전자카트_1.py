# 전자카트
# 1042 1313

import sys

sys.stdin = open("sample_input.txt")

class Permut:
    permutated_list = []
    result_list = []

    def __init__(self, given_list, pick_count) -> None:
        self.given_list = given_list
        self.pick_count = pick_count
        self.list_length = len(given_list)
        self.is_picked_list = [0] * self.list_length
        Permut.permutated_list = []
        Permut.result_list = []

    def permutate(self):
        if len(Permut.permutated_list) == self.pick_count:
            Permut.result_list.append("".join(Permut.permutated_list))
            return
        for i in range(self.list_length):
            if not self.is_picked_list[i]:
                self.is_picked_list[i] = 1
                Permut.permutated_list.append(str(self.given_list[i]))
                Permut.permutate(self)
                Permut.permutated_list.pop()
                self.is_picked_list[i] = 0
        if 1 not in self.is_picked_list:
            return Permut.result_list


for test_count in range(1, int(input()) + 1):
    list_length = int(input())
    distance_list = [list(map(int, input().split()))
                     for _ in range(list_length)]
    numbers_list = list(range(1, list_length))
    permut = Permut(numbers_list, len(numbers_list))
    min_result_sum = float("inf")
    for i in permut.permutate():
        result_sum = 0
        prev_num = 0
        for j in i:
            result_sum += distance_list[prev_num][int(j)]
            prev_num = int(j)
        result_sum += distance_list[prev_num][0]
        if result_sum < min_result_sum:
            min_result_sum = result_sum
    print(f"#{test_count}", min_result_sum)
