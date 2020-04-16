def solution(n):
    answer = 1
    for i in range(1,n):
        s = i
        for j in range(i+1, n):
            if s + j == n:
                answer += 1
                break
            elif s + j < n:
                s += j
            else:
                break
    return answer