def solution(n):
    answer = 0
    a = 0
    b = 1
    for i in range(2,n+1):
        tmp = b
        b = b + a
        a = tmp
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    else:
        answer = b
    return answer % 1234567