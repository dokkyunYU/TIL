incoming_str = list(input())

for looking_for in range(1, len(incoming_str)):
    if (incoming_str[looking_for] == incoming_str[0]) & (
        looking_for <= len(incoming_str) / 2 + 1
    ):
        for looking_for2 in range(1, looking_for):
            if incoming_str[looking_for2] != incoming_str[looking_for2]:
                break
            elif looking_for2 == looking_for - 1:
                print(looking_for)
                break
    elif looking_for == len(incoming_str) - 1:
        print('No pattern')

# 미완성 코드
