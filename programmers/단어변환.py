min = 217000000
def solution(begin, target, words):
    global min
    ch = [0]*len(words)
    if words.count(target) == 0:
        min = 0
    else:
        DFS(0, begin, target, words, ch)
        if min == 217000000:
            min = 0
    return min


def DFS(L, now, target, words, ch):
    global min
    if now == target:
        if min > L:
            min = L
        return
    else:
        for i in range(len(ch)):
            cnt = 0
            if ch[i] == 0:
                for x, y in zip(now, words[i]):
                    if x == y:
                        cnt += 1
                if cnt == len(words[i])-1:
                    ch[i] = 1
                    DFS(L+1, words[i], target, words, ch)
                    ch[i] = 0