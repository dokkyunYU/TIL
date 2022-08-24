import sys

sys.stdin = open("input.txt")


class StudentBinary:
    def __init__(self, all_page, aim):
        self.page_left = 1
        self.page_right = all_page
        self.page_center = 0
        self.aim = aim
        self.search_count = 0

    def search(self):
        while True:
            self.page_center = int((self.page_left + self.page_right) / 2)
            self.search_count += 1
            if self.page_center == self.aim:
                return self.search_count
            elif self.page_center > self.aim:
                self.page_right = self.page_center
            elif self.page_center < self.aim:
                self.page_left = self.page_center


T = int(input())

for test_count in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    A = StudentBinary(P, Pa)
    B = StudentBinary(P, Pb)

    A_count = A.search()
    B_count = B.search()

    if A_count == B_count:
        print(f"#{test_count}", 0)
    else:
        print(f"#{test_count}", "A" if A_count < B_count else "B")

# 0.20
