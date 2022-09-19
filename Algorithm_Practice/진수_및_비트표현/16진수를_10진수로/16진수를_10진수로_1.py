import sys

sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    numbers_string = input()
    bit_number_string = ""
    string_length = 0
    for i in numbers_string:
        for j in range(3, -1, -1):
            bit_number_string += str(1 if int(i, 16) & 1 << j else 0)
            string_length += 1
            if string_length == 7:
                print(int(bit_number_string, 2), end=" ")
                bit_number_string = ""
                string_length = 0
    print(int(bit_number_string, 2))
