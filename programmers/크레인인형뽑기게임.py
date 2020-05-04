from collections import deque

def solution(board, moves):
    answer = 0
    li = []
    for x in zip(*board):
        li.append(deque(x))
    bucket = deque()
    
    for x in li:
        while True:
            if x[0] == 0:
                x.popleft()
            else:
                break
    
    for x in moves:
        if len(li[x-1]) > 0:
            tmp = li[x-1].popleft()
        else:
            continue
            
        if len(bucket) == 0:
            bucket.append(tmp)
        else:
            if bucket[-1] == tmp:
                bucket.pop()
                answer += 2
            else:
                bucket.append(tmp)
    return answer