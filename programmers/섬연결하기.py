def findParent(ch, n):
    if n == ch[n]:
        return n
    else:
        return findParent(ch,ch[n])

def union(ch, a, b):
    a = findParent(ch,a)
    b = findParent(ch,b)
    if a < b:
        ch[b] = a
        return True
    elif a > b:
        ch[a] = b
        return True
    else:
        return False

def solution(n, costs):
    cnt = 0
    answer = 0
    costs = list(sorted(costs, key = lambda k : k[2]))
    ch = []
    for i in range(n):
        ch.append(i)

    for x in costs:
        if cnt == n-1:
            break
        if union(ch,x[0],x[1]):
            answer += x[2]
            cnt += 1 
    return answer