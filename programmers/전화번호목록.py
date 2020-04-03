def solution(phone_book):
    answer = True
    p = dict()
    for x in phone_book:
        p[x] = 1
    for x in phone_book:
        for i in range(1,len(x)):
            if x[0:i] in p:
                answer = False
                return answer
    return answer