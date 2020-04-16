def solution(A,B):
    answer = 0
    A1 = sorted(A)
    B1 = list(reversed(sorted(B)))
    for a,b in zip(A1,B1):
        answer += a*b
    return answer