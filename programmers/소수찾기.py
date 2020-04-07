from itertools import permutations

def getPrimeCheckList(num):
    ch = [0]*(num+1)
    ch[0] = 1
    ch[1] = 1
    for i in range(2,num+1):
        if ch[i] == 0:
            for j in range(2,num+1):
                x = i*j
                if x > num:
                    break
                else:
                    ch[x] = 1
    return ch

def combinatinList(numbers):
    b = []
    a = set()
    for i in range(1, len(numbers)+1):
        a.update(list(map(''.join, permutations(numbers, i))))
    a = list(a)
    for x in a:
        if x[0] != '0':
            b.append(x)
    return b

def CheckPrime(comList, chList):
    cnt = 0
    for x in comList:
        if chList[int(x)] == 0:
            cnt += 1
    return cnt

def solution(numbers):
    comList = combinatinList(numbers)
    maxN = max(comList)
    chList = getPrimeCheckList(int(maxN))
    answer = CheckPrime(comList,chList)
    return answer