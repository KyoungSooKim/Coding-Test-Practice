def solution(nums):
    answer = 0
    d = {}
    for x in nums:
        d[x] = d.get(x,0) + 1
    if len(nums)//2 <= len(d):
        answer = len(nums)//2
    else:
        answer = len(d)
    return answer