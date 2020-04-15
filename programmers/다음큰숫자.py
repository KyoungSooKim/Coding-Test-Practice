def solution(n):
    answer = 0
    cnt = 0
    tmp = bin(n)[2:]
    tmp = list(reversed(tmp))
    tmp.append('0')
    for i in range(0, len(tmp)-1):
        if tmp[i] == '1' and tmp[i+1] == '0':
            tmp[i+1] = '1'
            tmp[i] = '0'
            for j in range(0,i):
                if cnt > j:
                    tmp[j] = '1'
                else:
                    tmp[j] = '0'
            break
        elif tmp[i] == '1':
            cnt += 1
    tmp = "".join(list(reversed(tmp)))
    return int(tmp,2)