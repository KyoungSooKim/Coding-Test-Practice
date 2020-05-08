def solution(N):
    a = 1
    b = 1
    for _ in range(N-1):
        tmp = a
        a = b
        b = tmp + b
    return ( a + b ) * 2