# [BOJ] 1074. Z
# 소요 시간 : 00분

N, r, c = map(int, input().split())

start_sum = 0

for i in range(N - 1, 0, -1):
    num = 2**i
    num2 = num * num
    start_sum += ((r // num) * 2 + c // num) * num2
    r = r % num
    c = c % num

print(start_sum + 2 * r + c)

#########################################################

n, r, c = map(int, input().split())
r = bin(r)[2:].zfill(n)
c = bin(c)[2:].zfill(n)
s = 0
for i in range(1, n + 1):
    s += 2 ** (2 * n - 2 * i) * (int(c[i - 1]) + 2 * int(r[i - 1]))
print(s)
