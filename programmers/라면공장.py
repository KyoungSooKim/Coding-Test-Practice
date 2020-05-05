import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    li = []
    for day, sup in zip(dates, supplies):
        while day - stock > 0:
            stock += -1*heapq.heappop(li) 
            answer += 1
        heapq.heappush(li,-1*sup)
    if k > stock:
        while k > stock:
            stock += -1*heapq.heappop(li) 
            answer += 1
    return answer