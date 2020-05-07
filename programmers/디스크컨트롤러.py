import heapq
from collections import deque
def solution(jobs):
    answer = 0
    end = 0
    li = []
    l = len(jobs)
    jobs = deque(list(sorted(jobs)))
    i = 0
    while True:
        if len(jobs) == 0 and len(li) == 0:
                break  
        while len(jobs) != 0 and jobs[0][0] == i:
            heapq.heappush(li,(jobs[0][1], jobs[0][0]))
            jobs.popleft()
        if end == i:
            if len(li) == 0:
                end += 1
            else:
                tmp = heapq.heappop(li)
                end += tmp[0]
                answer += end - tmp[1]
        i += 1
    return answer//l