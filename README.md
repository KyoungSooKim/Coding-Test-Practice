# 프로그래머스 알고리즘 Reviews with python

## BFS/DFS

* queue : from collections import deque
* 상하좌우 : dx = [-1, 0, 1, 0], dy = [0, 1, 0, -1]
* 파이썬으로 재귀 사용시 필수 모듈 : import sys sys.setrecursionlimit(10**8)
* for구문으로 string 다루기 : for X in "abc" => X = a, b, c
* 깊은 복사 모듈 : import copy, copy.deepcopy(list) (shallow, deap copy reference: https://wikidocs.net/16038)
* 리스트 리버스 : list.reverse()
* 10진수 2진수로 변환 : bin(x)[2:] (문자의 앞 2개는 ob라서 슬라이싱함)
* rjust : "AB".rjust(5,'1') == "111AB"
* replace : "AB".replace('1', '#') == "###AB"

## Sort

* 타입확인 : type()
* '@'.join(list)  ex : a@b@c  (자주 사용하자)
*  sort 비교조건 함수화 (강력함) :
   * function functools import cmp_to_key
   * list로 반환한다  sorted(list, key = cmp_to_key(function))
   * function 반환값 -1, 0 , 1
* 리스트 다루기 : for i, v in enumerate(list)
