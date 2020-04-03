def solution(clothes):
    answer = 1
    p = dict()
    for x,y in clothes:
        p[y] = p.get(y, 0) + 1
    for x in p.values():
        answer = answer * (x + 1) 
    return answer - 1