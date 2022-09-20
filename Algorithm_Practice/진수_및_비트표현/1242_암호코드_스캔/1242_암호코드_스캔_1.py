# 암호코드 스캔
# 1026

import sys

sys.stdin = open("input.txt")

# 0:3211 -1:2221 -2:2122 -3:1411 -4:1132 -5:1231 -6:1114 -7:1312 -8:1213 -9:3112
numbers_3d_list = [-1,
                   [-1, [-1, 6, -1, 4], [-1, 8, -1, 5], [-1, 7], [-1, 3]],
                   [-1, [-1, -1, 2], [-1, -1, 1]],
                   [-1, [-1, 9], [-1, 0]]
                   ]
for test_count in range(1, int(input()) + 1):
    arr_height, arr_width = map(int, input().split())
    already_solved = []
    all_result_sum = 0
    for _ in range(arr_height):
        zero_counter = 0
        given_string = ""
        cipher_code_list = []
        for j in input()[:arr_width]:
            if j != "0" and zero_counter > 0:
                zero_counter = 0
            if given_string:
                given_string += j
            if j != "0" and not given_string:
                given_string += j
            if j == "0" and given_string:
                zero_counter += 1
                if zero_counter > 1:
                    cipher_code_list.append(given_string.strip("0"))
                    if cipher_code_list[-1] in already_solved:
                        cipher_code_list.pop()
                    zero_counter = 0
                    given_string = ""
        if given_string:
            cipher_code_list.append(given_string.strip("0"))
            if cipher_code_list[-1] in already_solved:
                cipher_code_list.pop()
        # if cipher_code_list:
        #     print(cipher_code_list)
        zero_counter = 0
        given_string = ""
        if not cipher_code_list:
            given_string = ""
            continue
        already_solved += cipher_code_list
        for cipher_code in cipher_code_list:
            cipher_code_string = ""
            for i in cipher_code:
                i = int(i, 16)
                # if i == 0:
                #     cipher_code_string += "0"
                # else:
                for k in range(3, -1, -1):
                    cipher_code_string += "1" if i & 1 << k else "0"
            cipher_code_string = cipher_code_string.strip("0")
            # print(cipher_code_string, len(cipher_code_string) % 56)
            if len(cipher_code_string) % 56:
                cipher_code_string = "0" * (56 - len(cipher_code_string) % 56) + cipher_code_string
            # print(cipher_code_string)
            # for k in range(0, len(cipher_code_string), 7):
            #     print(cipher_code_string[k:k+7])
            thickness = len(cipher_code_string) // 56
            prev_num = "0"
            counting_01 = 0
            idx_pointer = [0, 0, 0, 0]
            xyzq = 0
            answer_list = []
            for t in cipher_code_string:
                if prev_num != t:
                    idx_pointer[xyzq] = counting_01 // thickness
                    xyzq += 1
                    counting_01 = 1
                    if xyzq > 3:
                        x, y, z, q = idx_pointer
                        print(cipher_code_string)
                        print(cipher_code_list)
                        print(already_solved)
                        print(len(cipher_code_string.strip("0")))
                        print(thickness)
                        print(x, y, z)
                        print(prev_num, t)
                        answer_list.append(numbers_3d_list[x][y][z])
                        xyzq = 0
                else:
                    counting_01 += 1
                prev_num = t
            x, y, z, q = idx_pointer
            answer_list.append(numbers_3d_list[x][y][z])
            # print(answer_list)
            result_sum = 0
            for num in range(len(answer_list) - 1):
                if (num + 1) & 1:
                    result_sum += answer_list[num] * 3
                else:
                    result_sum += answer_list[num]
            all_result_sum += sum(answer_list) if (result_sum + answer_list[-1]) % 10 == 0 else 0
    print(f"#{test_count}", all_result_sum)
