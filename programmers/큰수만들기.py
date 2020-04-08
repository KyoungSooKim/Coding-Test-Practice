from collections import deque
 
def solution(number, k):
    m = 0
    while k > 0:
        for i in range(m,len(number)-1):
            if number[i] < number[i+1]:
                number = number[:i] + number[i+1:]
                k -= 1
                m = i-1
                if m < 0:
                    m = 0
                break
        else:
            number = number[:-1]
            k -= 1
    return number