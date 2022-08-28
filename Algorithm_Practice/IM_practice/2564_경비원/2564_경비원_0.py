import sys

input = sys.stdin.readline
stra, up = map(int, input().split())
stores = int(input())
loc = []
num = []
count = 0
for i in range(stores + 1):
    loc.append(list(map(int, input().split())))

for i in loc:
    if i[0] == 1:
        num.append(i[1])
    elif i[0] == 2:
        num.append(2 * stra + up - i[1])
    elif i[0] == 3:
        num.append(2 * stra + 2 * up - i[1])
    else:
        num.append(stra + i[1])
dongjun = num[-1]
for j in range(stores):
    X, Y = min(dongjun, num[j]), max(dongjun, num[j])
    count += min(Y - X, 2 * stra + 2 * up - Y + X)
print(count)
