# 이진수
# 0915 0954

import sys
sys.stdin = open("sample_input.txt")

for test_count in range(1, int(input()) + 1):
    print("#{}".format(test_count), end=" ")
    num_length, hex_num = input().split()
    for i in hex_num:
        i = int(i, 16)
        for j in range(3, -1, -1):
            print("1" if i & 1 << j else "0", end="")
    print()