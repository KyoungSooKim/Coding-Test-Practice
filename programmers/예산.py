def solution(budgets, M):
    answer = 0    
    right = M
    left = 1
    if sum(budgets) <= M:
        return max(budgets)
    while left <= right:
        mid = (right + left)//2
        s = 0
        for x in budgets:
            if mid >= x:
                s += x
            else:
                s += mid
        if s > M:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer