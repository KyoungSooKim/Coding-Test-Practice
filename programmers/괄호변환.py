from collections import deque
import sys
sys.setrecursionlimit(10**6)
answer = ''
def solution(p):
    global answer
    p = deque(p)    
    recursion(p, '', 0, 0)
    return answer

def recursion(p, u, L, R):
    global answer
    if len(p) == 0:
        return 
    now = p.popleft()
    u += now
    if now == '(':
        L += 1
    else:
        R += 1
    if L == R:
        if u[0] == '(' and u[-1] == ')':
            answer += u
            recursion(p, '', 0, 0)
            return 
        else:
            answer += '('
            recursion(p, '', 0 , 0)
            answer += ')'
            for i in range(1, len(u)-1):
                if u[i] == '(':
                    answer += ')'
                else:
                    answer += '('
            return
    else:
        recursion(p, u ,L, R)
        return