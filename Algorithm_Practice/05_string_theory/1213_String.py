import sys

sys.stdin = open("input.txt", encoding="UTF-8")

for test_count in range(1, 11):
    test_number = input()
    find_word = input()
    long_string = input()
    alpha_count = 0
    for idx, word in enumerate(long_string):
        if (
            # 찾는 문자의 첫 문자가 나오면 찾는 문자의 길이만큼 문자열 슬라이싱 이후 비교
            word == find_word[0]
            and long_string[idx : idx + len(find_word)] == find_word
        ):
            alpha_count += 1

    print(f"#{test_number}", alpha_count)

# 0.30
