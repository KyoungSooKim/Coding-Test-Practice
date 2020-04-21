def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    d1 = {}
    d2 = {}
    d3 = {}
    d4 = {}
    for i in range(0,len(str1)-1):
        x = str1[i:i+2]
        if x.isalpha():
            d1[x] = d1.get(x,0) + 1
    for i in range(0,len(str2)-1):
        x = str2[i:i+2]
        if x.isalpha():
            d2[x] = d2.get(x,0) + 1
    for x in d1:
        if d2.get(x, 0) > 0:
            d3[x] = min(d1.get(x), d2.get(x))
        d4[x] = max(d1.get(x), d2.get(x,0))
    for x in d2:
        d4[x] = max(d1.get(x,0), d2.get(x))
    if len(d4) == 0:
        answer = 1
    else:
        answer = sum(d3.values())/sum(d4.values())
    return int(answer*65536)