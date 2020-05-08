def solution(routes):
    answer = 1
    routes = list(sorted(routes))
    right = 30000
    left = -30000
    for x in routes:
        if right <  x[0]:
            answer += 1
            right = x[1]
            left = x[0]
            print(x)
        else:            
            if x[0] > left:
                left = x[0]
            if x[1] < right:
                right = x[1]
    return answer