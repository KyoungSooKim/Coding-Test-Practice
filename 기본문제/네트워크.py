from collections import deque

def solution(n, computers):
    answer = 0
    dQ = deque()
    ch = [0]*n
    for i in range(n):   
        if ch[i] == 0:
            dQ.append(i)
            ch[i] = 1
        else:
            continue
        while dQ:
            now = dQ.popleft()
            for j in range(n):
                if computers[now][j] == 1 and ch[j] == 0:
                    dQ.append(j)
                    ch[j] = 1
        answer += 1
    return answer