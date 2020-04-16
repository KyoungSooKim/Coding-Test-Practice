def solution(s):
    answer = ''
    tmp = list(map(int, s.split()))
    tmp.sort()
    answer += str(tmp[0])
    answer += ' '
    answer += str(tmp[-1])
    return answer