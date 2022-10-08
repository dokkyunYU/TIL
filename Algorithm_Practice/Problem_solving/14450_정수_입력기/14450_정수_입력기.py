import sys

sys.stdin = open("input.txt")

for test_count in range(1, 1 + int(input())):
    left, right, qnum = map(int, input().split())
    left = "0" * (len(right) - len(left)) + left
    print(f"#{test_count} ", end="")
    for k in input().split():
        num_str = ""
        r_len = len(right)
        num_len = len(k)
        if num_len > r_len:
            print("X", end="")
            continue
        for i, j in enumerate(k):
            num_str += j
            if (
                not (int(left[: i + 1]) <= int(num_str) <= int(right[: i + 1]))
                and i + 1 >= r_len - 1
            ):
                print("X", end="")
                break
        else:
            print("O", end="")
    print()
