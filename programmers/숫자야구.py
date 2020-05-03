import copy

def solution(baseball):
    answer = 0
    tmp = sorted(baseball, key = lambda x : (x[1],x[2]), reverse=True)
    for a in range(111,1000):
        m = list(map(int,str(a)))
        
        if m.count(0) > 0:
            continue   
        if len(set(m)) < 3:
            continue
        cnt = 0
        for x in baseball:
            n = copy.deepcopy(m)
            strike = 0 
            ball = 0
            tmp = list(map(int,str(x[0])))
            
            for i in range(3):
                if tmp[i] == n[i]:
                    tmp[i] = -1
                    n[i] = -2
                    strike += 1
            for i in range(3):
                if tmp[i] == n[0]:
                    tmp[i] = -1
                    n[0] = -2
                    ball += 1
            for i in range(3):
                if tmp[i] == n[1]:
                    tmp[i] = -1
                    n[1] = -2
                    ball += 1
            for i in range(3):
                if tmp[i] == n[2]:
                    tmp[i] = -1
                    n[2] = -2
                    ball += 1
            if x[1] == strike and x[2] == ball:
                cnt += 1
            else:
                break
        if cnt == len(baseball):
            answer += 1
    return answer