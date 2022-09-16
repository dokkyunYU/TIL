# 세제곱근을 찾아라
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXVyCaKugQDFAUo
# 0926 1011

import sys
import math
sys.stdin = open("sample_input.txt")

for test_count in range(1, int(input()) + 1):
    the_number = int(input())
    answer = math.pow(the_number, 1/3)
    answer = round(answer) if math.isclose(round(answer), answer) else -1
    print(f"#{test_count}", answer)
