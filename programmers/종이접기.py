def solution(n):
    answer = []
    toggle = [1,0]
    for i in range(n):
        tmp = [0]
        j = 0
        for x in answer:
            tmp.append(x)
            tmp.append(toggle[j%2])
            j += 1
        answer = tmp
    return answer