import heapq

def solution(n, works):
    answer = 0
    li = []
    for x in works:
        heapq.heappush(li,-1*x)
    for _ in range(n):
        if not li:
            break
        tmp = -1*heapq.heappop(li)
        tmp -= 1
        if tmp == 0:
            continue
        else:
            heapq.heappush(li,-1*tmp)
    for x in li:
        answer += x*x
    return answer