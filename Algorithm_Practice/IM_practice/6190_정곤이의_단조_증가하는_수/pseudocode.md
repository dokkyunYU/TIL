# 문제의 개념

작은 자리수로 갈 수록 자리값이 점점 커지는 수를 단조증가하는 수라고 한다.

양의 정수 N개가 주어질때 그중 두개의 숫자의 곱이 단조증가하는 수 인것을 찾고, 그 중 최대값을 구하라


# pseudocode

```
def is_this_danzo(num: int) -> int:
  strnum = str(num)
  prv_num = 0
  for i in strnum:
    if prv_num > int(i):
      return 0
    prv_num = int(i)
  return 1


input = N
input = int_list: list =  int[1 ~ N]
max_value = 0
for i in range(N):
  for j in range(i + 1, N):
    if (
      mult_num = int_list[i] * int_list[j]
      is_this_danzo(mult_num) and
      max_value < mult_num
      )
      max_value = mult_num
print(max_value)
```