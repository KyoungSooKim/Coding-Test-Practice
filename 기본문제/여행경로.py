import copy
result = []
def solution(tickets):
    global result
    DFS(0, ['ICN'], [0]*len(tickets) ,tickets)
    if len(result) > 1:
        nowList = result.pop(0)
        while result:
            nextList = result.pop(0)
            for x, y in zip(nowList, nextList):
                if x != y:
                    if x > y:
                        nowList = copy.deepcopy(nextList)   
                    break
    else:
        nowList = result.pop(0)
    return nowList

def DFS(L, path, ch, tickets):
    global result
    
    if L == len(tickets):
        result.append(copy.deepcopy(path))
        return
    else:
        for i in range(len(ch)):
            if ch[i] == 0 and path[-1] == tickets[i][0]:
                ch[i] = 1
                path.append(tickets[i][1])
                DFS(L+1, path, ch, tickets)
                path.pop()
                ch[i] = 0