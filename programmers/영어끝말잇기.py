def solution(n, words):
    answer = []
    d = {}
    cnt = 1
    bef = words[0]
    d[bef] = 1
    for x in words[1:]:
        cnt += 1
        d[x] = d.get(x,0) + 1
        if d[x] > 1 or bef[-1] != x[0]:
            print(x)
            if cnt%n == 0:
                answer.append(n)
                answer.append(cnt//n)
            else:
                answer.append(cnt%n)
                answer.append(cnt//n + 1)
            break
        else:
            bef = x
    else:
        answer.append(0)
        answer.append(0)
    return answer