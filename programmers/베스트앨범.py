def solution(genres, plays):
    answer = []
    genresSort = {}
    playSum = {}
    i = 0
    for x,y in zip(genres, plays):
        tmp = genresSort.get(x,[])
        tmp.append((i, y))
        genresSort[x] = tmp
        playSum[x] = playSum.get(x,0) + y
        i += 1
        
    playSum = sorted(playSum.items(), key = lambda x : -x[1] )
    
    for gen,plays in playSum:
        tmp = genresSort[gen]
        tmp = sorted(tmp, key = lambda x: ( -x[1], x[0]))
        answer.append(tmp[0][0])
        if len(tmp) >= 2:
            answer.append(tmp[1][0])    
    return answer