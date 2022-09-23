import sys

sys.stdin = open("input.txt", encoding="utf-8")

cipher_code_list = [
    "0001101",
    "0011001",
    "0010011",
    "0111101",
    "0100011",
    "0110001",
    "0101111",
    "0111011",
    "0110111",
    "0001011",
]
for test_count in range(1, int(input()) + 1):
    height, width = map(int, input().split())
    cipher_code_string = ""
    already_inputed = False
    for _ in range(height):
        if already_inputed:
            input()
            continue
        cipher_code_string = input()
        if "1" in cipher_code_string:
            already_inputed = True
    string_idx = 0
    order_number = 0
    is_proper_code = 0
    result_sum = 0
    print(cipher_code_string)
    while string_idx < width:
        sliced_cipher_string = cipher_code_string[string_idx : string_idx + 7]
        string_idx += 7
        print(sliced_cipher_string)
        if sliced_cipher_string == "0000000":
            continue
        if order_number == 8:
            break
        for i in range(10):
            if sliced_cipher_string == cipher_code_list[i]:
                order_number += 1
                result_sum += i
                if order_number & 1:
                    is_proper_code += i * 3
                else:
                    is_proper_code += i
                break
    print(result_sum, is_proper_code)
    print(f"#{test_count}", result_sum if is_proper_code % 10 == 0 else 0)
