def solution(arr1, arr2):
    answer =[]
    at = [[y for y in x] for x in zip(*arr2)]
    for x in arr1:
        a = []
        for y in at:
            s = 0
            for i in range(len(x)):
                s += x[i]*y[i]
            a.append(s)
        answer.append(a)      
    return answer