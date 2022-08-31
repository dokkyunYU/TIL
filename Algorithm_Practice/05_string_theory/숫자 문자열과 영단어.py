number_word_list = [
    ["0", "zero"],
    ["1", "one"],
    ["2", "two"],
    ["3", "three"],
    ["4", "four"],
    ["5", "five"],
    ["6", "six"],
    ["7", "seven"],
    ["8", "eight"],
    ["9", "nine"],
]
given_word = input()
for i in number_word_list:
    # 문자를 찾아서 숫자로 바꾼다
    given_word = given_word.replace(i[1], i[0])
print(int(given_word))

# 0.20
