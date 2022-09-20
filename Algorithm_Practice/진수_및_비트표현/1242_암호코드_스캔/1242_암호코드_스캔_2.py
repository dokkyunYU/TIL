# 암호코드 스캔
# 1601

import sys

sys.stdin = open("sample_input.txt")

# 0:3211 -1:2221 -2:2122 -3:1411 -4:1132 -5:1231 -6:1114 -7:1312 -8:1213 -9:3112
# 0:112 1:122 2:221 3:114 4:231 5:132 6:411 7:213 8:312 9:211
numbers_dict = {112: 0, 122: 1, 221: 2, 114: 3, 231: 4, 132: 5, 411: 6, 213: 7, 312: 8, 211: 9}
for test_count in range(1, int(input()) + 1):
    arr_height, arr_width = map(int, input().split())
    all_result_sum = 0
    for _ in range(arr_height):
        hex_arr = input()
        binary_arr = ""
        for i in hex_arr:
            i = int(i, 16)
            for j in range(3, -1, -1):
                binary_arr += "1" if i & 1 << j else "0"
        reverse_proportion_list = []
        number_counter = 0
        counter_string = ""
        zero_counter = 0
        count_of_1 = 0
        already_solved = []
        for k in range(len(binary_arr) - 1, -1, -1):
            if len(reverse_proportion_list) == 8:
                result_sum = 0
                auth_sum = 0
                reverse_proportion_list = reverse_proportion_list[::-1]
                solved_string = ""
                for t in range(len(reverse_proportion_list)):
                    solved_string += reverse_proportion_list[t]
                    tt = int(reverse_proportion_list[t]) // min(list(map(int, reverse_proportion_list[t])))
                    result_sum += numbers_dict[tt]
                    if (t+1) & 1:
                        auth_sum += numbers_dict[tt] * 3
                    else:
                        auth_sum += numbers_dict[tt]
                if solved_string in already_solved:
                    reverse_proportion_list = []
                    continue
                else:
                    already_solved.append(solved_string)
                if auth_sum % 10 == 0:
                    all_result_sum += result_sum
            if count_of_1 == 2 and binary_arr[k] == "0":
                counter_string += str(number_counter)
                reverse_proportion_list.append(counter_string)
                counter_string = ""
                number_counter = number_counter * int(binary_arr[k]) + int(binary_arr[k])
                count_of_1 = 0
            if binary_arr[k] == "0" and number_counter:
                counter_string += str(number_counter)
                count_of_1 += 1
            number_counter = number_counter * int(binary_arr[k]) + int(binary_arr[k])
            if counter_string and binary_arr[k] == "0":
                zero_counter += 1
            if zero_counter and number_counter:
                counter_string += str(zero_counter)
                count_of_1 += 1
                zero_counter = 0
    print(all_result_sum)
