# 프로그래머스 알고리즘 Reviews with python

BFS/DFS

1. queue: from collections import deque
2. 상하좌우: dx = [-1, 0, 1, 0], dy = [0, 1, 0, -1]
3. 재귀 리미트: import sys sys.setrecursionlimit(10**8)
4. string for문 : for X in "abc" => X = a, b, c
5. 깊은 복사: import copy, copy.deepcopy(list) (shallow, deap copy reference: https://wikidocs.net/16038)
6. 리스트 리버스: list.reverse()
7. 10진수 2진수로 변환: bin(x)[2:] (문자의 앞 2개는 ob라서 슬라이싱함)
8. rjust: "AB".rjust(5,'1') == "111AB"
9. replace: "AB".replace('1', '#') == "###AB"

Sort

1. type() 타입확인
2. '@'.join(list)  ex(a@b@c)
3. function functools import cmp_to_key
   list로 반환한다  sorted(list, key = cmp_to_key(function))
   function 반환값 -1, 0 , 1
4. for i, v in enumerate(list)
