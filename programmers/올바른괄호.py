def solution(s):
    answer = True
    t = []
    for x in s:
        if x == '(':
            t.append(x)
        else:
            if not t:
                answer = False
                break
            else:
                t.pop()
    if t:
        answer = False
    return answer