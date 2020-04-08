from collections import deque

def checker(t, s):
    for x in s:
        if t[0] == x:
            t.popleft()
            if not t:
                break
    if t:
        for x in t:
            if s.count(x):
                return 0
    return 1
        

def solution(skill, skill_trees):
    answer = 0
    for x in skill_trees:
        answer += checker(deque(skill), list(x))        
    return answer