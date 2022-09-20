# 이진수 2
# 0956 1020
import sys
import math
sys.stdin = open("sample_input.txt")

for test_count in range(1, int(input()) + 1):
    number_under_1 = float(input())
    result_string = ""
    for upper_num in range(-1, -13, -1):
        if math.isclose(number_under_1, 2 ** upper_num):
            result_string += "1"
            break
        elif number_under_1 > 2 ** upper_num:
            number_under_1 -= 2 ** upper_num
            result_string += "1"
        else:
            result_string += "0"
    else:
        result_string = "overflow"
    print(f"#{test_count}", result_string)