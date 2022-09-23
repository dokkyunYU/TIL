# 최대상금
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD
# 1800

import sys
# from collections import deque

sys.stdin = open("input.txt")


def exchanging(change_count):
    if not change_count:
        number = int("".join(numbers_list))
        if number not in result_list:
            result_list.append(number)
        return
    for i in range(list_length):
        for j in range(i, list_length):
            numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]
            exchanging(change_count - 1)
            numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]


for test_count in range(1, int(input()) + 1):
    numbers_string, exchange_string = input().split()
    exchange_count = int(exchange_string)
    numbers_list = list(numbers_string)
    list_length = len(numbers_list)
    result_list = []
    exchange_dict = {}
    # exchanging(exchange_count)
    dict_queue = ["".join(numbers_list)]
    while dict_queue:
        key_int = dict_queue.pop(0)
        value_list = []
        numbers_list = list(key_int)
        dict_value = exchange_dict.get(key_int)
        if dict_value:
            dict_queue += dict_value
        for i in range(list_length - 1):
            for j in range(i + 1, list_length):
                numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]
                value_list.append("".join(numbers_list))
                numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]
        exchange_dict.update([(key_int, value_list)])
        dict_queue += exchange_dict[key_int]
        if len(exchange_dict) == 5:
            break
    print("#{} {}".format(test_count, exchange_dict))
