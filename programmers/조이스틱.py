def leftRight(ch, length):
    if not ch:
        return 0
    step1 = max(ch)
    ch2 = []
    for x in ch:
        ch2.append(length - x)
    step2 = max(ch2)
    a = 217000000
    b = 217000000
    for x in ch:
        if length//2 > x:
            a = x
        else:
            b = length - x
            break
    step3 = a + b + a
    step4 = b + b + a
    return min(step1,step2,step3,step4)
        
def makeChList(name):
    s = 'A'* len(name)
    ch = []
    for i in range(1, len(name)):
        if s[i] != name[i]:
            ch.append(i)
    return ch

def upDown(name):
    tot = 0
    s = 'A' * len(name)
    for i in range(0,len(name)):
        if s[i] != name[i]:
            a = ord(name[i]) - ord('A')
            b = ord('Z') - ord(name[i]) + 1
            tot += min(a,b)
    return tot
        
def solution(name):
    ch = makeChList(name)
    step = leftRight(ch, len(name))
    step += upDown(name)
    return step