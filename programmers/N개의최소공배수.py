import copy

def solution(arr):
    answer = 1
    arr2 = [1]
    while True:
        m = max(arr)
        
        for i in range(2,m+1):
            li = []
            cnt = 0
            for x in arr:
                if x%i == 0:
                    li.append(x//i)
                    cnt += 1
                else:
                    li.append(x)
            if cnt >= 2:
                arr = copy.deepcopy(li)
                arr2.append(i)
                break
        else:
            break
    for x in arr2:
        answer *= x
    for x in arr:
        answer *= x
    return answer