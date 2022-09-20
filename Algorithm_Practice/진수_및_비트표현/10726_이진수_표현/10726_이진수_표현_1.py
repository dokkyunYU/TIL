# 이진수 표현
# 1736 1740

import sys
sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    bit_counter = 0
    for i in range(n):
        if m & 1 << i:
            bit_counter += 1
    print(f"#{test_count}", "ON" if bit_counter == n else "OFF")