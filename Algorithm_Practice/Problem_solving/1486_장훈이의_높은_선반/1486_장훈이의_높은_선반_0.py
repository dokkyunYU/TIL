def res(i, chong_ki):
    global ki_cha
    if B <= chong_ki < ki_cha:
        ki_cha = chong_ki
    if i == N:
        return
    res(i + 1, chong_ki)
    res(i + 1, chong_ki + ki[i])


T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    ki = list(map(int, input().split()))
    ki_cha = 200000
    res(0, 0)
    print(f'#{t + 1} {ki_cha - B}')
