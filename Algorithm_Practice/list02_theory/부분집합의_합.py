import sys


def change_to_binary(given_number):
    if given_number < 0:
        return 0
    elif given_number == 0:
        return "0"
    elif given_number == 1:
        return "1"
    else:
        return change_to_binary(given_number // 2) + str(given_number % 2)


sys.stdin = open("input.txt")


T = int(input())

for test_count in range(1, T + 1):
    numbers = 10

    numbers_list = list(map(int, input().split()))

    for i in range(1, 1 << numbers):
        # 000000000부터 111111111까지 즉 모든 요소에 대응하여 0 혹은 1이 배치될 수 있다.
        subset_sum = 0
        index_count = 0
        # 2진수 문자열로 변환후 문자열 내를 순환하며 1을 반환할때마다 그 위치의 숫자를 더한다.
        for j in change_to_binary(i):
            if j == "1":
                subset_sum += numbers_list[index_count]
            index_count += 1

        if subset_sum == 0:
            print("#{} 1".format(test_count))
            break
    else:
        print("#%d 0" % test_count)
