from collections import deque
def solution(cacheSize, cities):
    time = 0
    c = deque()
    for x in cities:
        x = x.upper()
        for i in range(len(c)):
            if c[i] == x and cacheSize != 0:
                time += 1
                if len(c) == cacheSize :     
                    del c[i]
                c.append(x)
                break
        else:
            time += 5
            if len(c) == cacheSize and cacheSize != 0:
                c.popleft()
            c.append(x)
    return time