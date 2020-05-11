def solution(s):
    answer = 0
    length = len(s)
    for i in range(length):
        for j in range(i+1):
            tmp = s[j:j+length-i]
            if tmp == tmp[::-1]:
                print(tmp)
                return length-i