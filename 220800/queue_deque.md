# from collections import deque

양방향에서 자료의 출입 가능

pop을 해도 O(1)만큼의 시간 복잡도 (queue는 pop을 하면 나머지 전부 인덱스를 당겨야해서 O(n)만큼 걸림)

from collections import deque

d = deque([1, 2, 3, 4])

pop, popleft, append, appendleft