import sys

sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    numbers_string = input()
    result_decimal_number = 0
    for i in range(len(numbers_string)):
        upper_number = 6 - i % 7
        result_decimal_number += int(numbers_string[i]) * (2**upper_number)
        if upper_number == 0:
            print(result_decimal_number, end=" ")
            result_decimal_number = 0
    print()
