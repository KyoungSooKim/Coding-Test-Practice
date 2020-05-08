def solution(n, times):
    answer = 0    
    right = n*(max(times))
    left = 1
    while left <= right:
        mid = (right + left)//2
        s = 0
        for x in times:
            s += mid//x
        if s >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer