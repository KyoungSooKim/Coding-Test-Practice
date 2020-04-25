def getList(x):
    tmp = x.split(',')
    return tmp

def getTime(x):
    li = getList(x)
    t1 = li[0].split(':')
    t2 = li[1].split(':')
    t3 = (int(t2[0]) - int(t1[0]))*60 + int(t2[1]) - int(t1[1])
    return t3

def getSong(x):
    li = getList(x)
    t = getTime(x)
    s = li[3]
    s = s.replace('C#','Q').replace('D#','W').replace('F#','R').replace('G#','T').replace('A#','Y')
    sLength = len(s)
    song = ''
    song += s*(t//sLength)
    song += s[0:t%sLength]
    return song

def solution(m, musicinfos):
    answer = []
    m = m.replace('C#','Q').replace('D#','W').replace('F#','R').replace('G#','T').replace('A#','Y')
    
    for x in musicinfos:
        s = getSong(x)
        if m in s: 
            answer.append(getList(x))
            answer[-1].append(getTime(x))
    if len(answer) == 0:
        answer = '(None)'
    elif len(answer) == 1:
        answer = answer[0][2]
    else:
        answer = sorted(answer, key = lambda k : -k[4])
        answer = answer[0][2] 
    return answer