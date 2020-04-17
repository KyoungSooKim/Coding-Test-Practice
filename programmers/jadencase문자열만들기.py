def solution(s):
    s = s.lower()
    L=s.split(" ")
    answer = ""
    for i in L:
        i= i.capitalize()
        answer+= i+" "
    return answer[:-1]
