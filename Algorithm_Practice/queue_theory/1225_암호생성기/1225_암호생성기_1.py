import sys

sys.stdin = open("input.txt")

for test_count in range(1, 11):
    test_number = int(input())
    number_queue = list(map(int, input().split()))

    while True:
        for i in range(1, 6):
            poping_number = number_queue.pop(0)
            if poping_number > i:
                number_queue.append(poping_number - i)
            else:
                number_queue.append(0)
                break
        if number_queue[-1] == 0:
            break

    print(f"#{test_count}", *number_queue)
