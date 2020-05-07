import heapq

def solution(operations):
    li = []
    li2 = []
    op = []
    for x in operations:
        tmp = x.split(" ")
        op.append((tmp[0], int(tmp[1])))
    for x in op:
        if x[0] == 'I':
            heapq.heappush(li,x[1])
            heapq.heappush(li2,-x[1])
        elif x[1] == 1:
            if len(li2) == 0:
                continue
            if li[0] == -1*li2[0]:
                if len(li) >= 2 and len(li2) >= 2 and li[1] == -1*li2[1]:
                    heapq.heappop(li2)
                    heapq.heappop(li)
                else:
                    li = []
                    li2 = []
            else:
                heapq.heappop(li2)
        else:
            if len(li) == 0:
                continue
            if li[0] == -1*li2[0]:
                if len(li) >= 2 and len(li2) >= 2 and li[1] == -1*li2[1]:
                    heapq.heappop(li2)
                    heapq.heappop(li)
                else:
                    li = []
                    li2 = []
            else:
                heapq.heappop(li)
    if len(li) == 0:
        answer = [0,0]
    else:
        answer = [-1*li2[0],li[0]]
    return answer