# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구한다


n = int(input())

my_list = list(range(1, n + 1))
print(sum(my_list[1::2]))
