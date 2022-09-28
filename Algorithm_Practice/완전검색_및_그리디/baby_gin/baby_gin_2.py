# Baby Gin
# run : 연속된 숫자 3개
# triplet : 동일한 숫자 3개
# 1605 1740


def comb(now_idx, run_select, tri_select):
    global is_baby_gin
    if is_baby_gin:
        return
    if run_select == 0 and tri_select == 0:
        is_run, is_tri = False, False
        if (
            run_select_list[0] + 1 == run_select_list[1]
            and run_select_list[1] + 1 == run_select_list[2]
        ):
            is_run = True
        if tri_select_list[0] == tri_select_list[1] == tri_select_list[2]:
            is_tri = True
        if is_run and is_tri:
            is_baby_gin = True
    if now_idx > numbers_list_length - 1:
        return
    if run_select > 0:
        run_select_list.append(numbers_list[now_idx])
        comb(now_idx + 1, run_select - 1, tri_select)
        run_select_list.pop()
    if tri_select > 0:
        tri_select_list.append(numbers_list[now_idx])
        comb(now_idx + 1, run_select, tri_select - 1)
        tri_select_list.pop()
    comb(now_idx + 1, run_select, tri_select)


for test_count in range(1, int(input()) + 1):
    numbers_list = list(map(int, input()))
    numbers_list.sort()
    numbers_list_length = len(numbers_list)
    run_select_list = []
    tri_select_list = []
    is_baby_gin = False
    comb(0, 3, 3)
    print(is_baby_gin)
