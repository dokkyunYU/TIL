import sys

# 각 숫자의 등장빈도를 나타낸 리스트를 받아서 triplet이 있다면 그 숫자들을 제외한 리스트를 반환
# parameter로 넘겨받은 리스트는 넘겨준 list의 얕은 복사본 (global numbers_count_sum is given_sum_list == True)
# 함수내에서 넘겨받은 리스트를 수정하면 global의 리스트도 수정됨
def is_there_triplet(given_sum_list):
    for i, k in enumerate(given_sum_list):
        if k >= 3:
            given_sum_list[i] -= 3
            return given_sum_list
    return False


# 각 숫자의 등장빈도를 나타낸 리스트를 받아서 run이 있다면 그 숫자들을 제외한 리스트를 반환
# parameter로 넘겨받은 리스트는 넘겨준 list의 얕은 복사본 (global numbers_count_sum is given_sum_list == True)
# 함수내에서 넘겨받은 리스트를 수정하면 global의 리스트도 수정됨
def is_there_run(given_sum_list):

    for i in range(1, len(given_sum_list) - 1):
        if given_sum_list[i] > 0 and given_sum_list[i + 1] > 0 and given_sum_list[i + 2] > 0:
            given_sum_list[i] -= 1
            given_sum_list[i + 1] -= 1
            given_sum_list[i + 2] -= 1
            return given_sum_list
    return False


sys.stdin = open("input.txt")

test_count = int(input())

for i in range(1, test_count + 1):
    # 각 숫자의 등장빈도를 리스트로 작성
    numbers_count_sum = [0] * 10
    numbers_list = list(map(int, input()))

    for j in numbers_list:
        numbers_count_sum[j] += 1

    is_this_babygin = 0
    # 리스트에 더이상 run 혹은 triplet이 없을때까지 반복
    while is_there_run(numbers_count_sum) or is_there_triplet(numbers_count_sum):
        is_this_babygin += 1

    # 리스트에 더이상 0 이외의 숫자가 없다면 1을 아니면 0을 표시
    for t in numbers_count_sum:
        if t != 0:
            print(f"#{i} 0")
            break
    else:
        print(f"#{i} 1")
