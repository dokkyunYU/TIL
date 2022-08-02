'''
1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.
'''
num1 = int(input())
num2 = 1
count_up = 1
while num2 + count_up < num1:
    num2 += count_up
    count_up += 1
print(num2, count_up)
