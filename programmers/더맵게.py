import heapq 

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True and answer >= 0:
        for x in scoville:
            if x < K:   
                if len(scoville) < 2:
                    answer = -1
                    break
                a = heapq.heappop(scoville)
                b = heapq.heappop(scoville)
                a = a + b*2
                heapq.heappush(scoville, a)
                answer += 1
                break
        else:
            break
    return answer