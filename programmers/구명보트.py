
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
from collections import deque

def solution(people, limit):
    answer = 0
    tmp = deque(sorted(people))

    while tmp:
        if len(tmp) == 1:
            tmp.pop()
            answer += 1
        elif tmp[0] + tmp[-1] <= limit:
            tmp.popleft()
            tmp.pop()
            answer += 1
        else:
            tmp.pop()
            answer += 1
    return answer