end_num = int(input())
for num1 in range(1, end_num + 1):
    num_str = list(str(num1))
    clap = num_str.count('3') + num_str.count('6') + num_str.count('9')
    if clap > 0:
        for clapping in range(0, clap):
            print('-', end='')
        print(' ', end='')
    else:
        print(num1, end=' ')
