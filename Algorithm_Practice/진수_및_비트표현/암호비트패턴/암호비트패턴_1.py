import sys

sys.stdin = open("input.txt", encoding="utf-8")

bit_cipher_list = [
    "001101",
    "010011",
    "111011",
    "110001",
    "100011",
    "110111",
    "001011",
    "111101",
    "011001",
    "101111",
]
for test_count in range(1, int(input()) + 1):
    numbers_string = input()
    bit_numbers_string = ""
    string_idx = 0
    cipher_number_list = []
    for i in numbers_string:
        for j in range(3, -1, -1):
            bit_numbers_string += str(1 if int(i, 16) & 1 << j else 0)
    while string_idx < len(bit_numbers_string):
        for t in range(10):
            if bit_numbers_string[string_idx : string_idx + 6] == bit_cipher_list[t]:
                cipher_number_list.append(t)
                string_idx += 6
                break
        else:
            string_idx += 1
    print(*cipher_number_list)
