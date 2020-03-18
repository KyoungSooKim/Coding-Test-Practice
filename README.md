# 프로그래머스 알고리즘 Reviews with python

BFS/DFS

1. from collectiions import deque
2. dx = [-1, 0, 1, 0], dy = [0, 1, 0, -1]
3. sys.setrecursionlimit(10**6) 재귀 리미트
4. for X in "abc" => X = a, b, c
5. import copy, copy.deapcopy(list) (shallow, deap copy reference: https://wikidocs.net/16038)

sort

1. type() 타입확인
2. '@'.join(list)  ex(a@b@c)
3. function functools import cmp_to_key
   list로 반환한다  sorted(list, key = cmp_to_key(function))
   function 반환값 -1, 0 , 1
4. for i, v in enumerate(list)
