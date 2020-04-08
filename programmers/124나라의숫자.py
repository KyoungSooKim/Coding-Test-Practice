def get(n):
    res = []
    while n != 0:
        tmp = n % 3
        if tmp == 0:
            tmp = 3
        n = n - tmp
        n = n // 3
        res.append(tmp)
        
    return list(reversed(res))

def solution(n):
    answer = ''
    res = get(n) 
    for x in res:
        if x == 3:
            answer += '4'
        elif x == 1:
            answer += '1'
        else:
            answer += '2'
    return answer