def solution(n, s):
    answer = []
    tmp = s//n
    if tmp == 0:
        answer.append(-1)
    else:
        tmp2 = s%n
        for _ in range(n-tmp2):
            answer.append(tmp)
        for _ in range(tmp2):
            answer.append(tmp+1)
    return answer