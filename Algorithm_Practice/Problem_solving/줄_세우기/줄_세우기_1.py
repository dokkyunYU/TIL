# 줄 세우기
# https://www.acmicpc.net/problem/1681
# input : 10 1
# output : 22

n, l = input().split()
lavel = 0
student = 0
while student < int(n):
    lavel += 1
    if l in str(lavel):
        continue
    student += 1
print(lavel)
