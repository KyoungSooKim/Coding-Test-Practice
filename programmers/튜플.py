def solution(s):
    answer = []
    t = []
    s = s[2:-2]
    s = s.split('},{')
    for x in s:
        t.append(list(map(int, x.split(','))))
    t = sorted(t, key = lambda k : len(k))
    
    for x in t:
        for y in answer:
            x.remove(y)
        answer.append(x[0])
        
    return answer