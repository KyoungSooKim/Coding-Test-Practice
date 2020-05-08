def solution(weight):
    weight = list(sorted(weight))
    s = 0
    for x in weight:
        if s + 1 < x:
            return s + 1
        else:
            s += x
    return s + 1