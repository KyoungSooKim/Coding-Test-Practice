# 프로그래머스 알고리즘 Reviews with python

## Union-Find (합집합 찾기)
<pre><code>
function getParent( parent, num ):
  if parent[num] == num: return num
  return parent[num] = getParent(ch, parent[num])
  
function unionParent( parent, a, b):
  a = getParent(parent, a)
  b = getParent(parent, b)
  if a < b: parent[b] = a
  else parent[a] = b
  
function findParent( parent, a , b):
  a = getParent(parent, a)
  b = getParent(parent, b)
  if a==b: return 1
  else return 0
</code></pre>

## 크루스칼 알고리즘 (그리디)
* 비용이 적은것부터 차근차근 더한다.
* findParent 함수로 서클이 생기는 경우는 패스한다.
* parent list는 연결관계를 나타낸다. (연결된 노드중 작은 노드 id를 저장한다, 초기값은 자신의 id)
<pre><code>
parent = [], list = [[0,1,1],[1,3,1],[0,2,2],[1,2,5],[2,3,8]] (정렬된 list)
cnt = 0 , answer = 0
for i in range(n):
  parent.append(i)
for x in list:
  if cnt == n-1:
    break
  if findParent(parent, x[0], x[1]):
      unionParent(parent, x[0], x[1])
      answer += x[2]
      cnt += 1
</code></pre>

## BFS/DFS
* recursion : import sys sys.setrecursionlimit(10**8)
* 상하좌우 : dx = [-1, 0, 1, 0], dy = [0, 1, 0, -1]

## DEQUE
* queue : from collections import deque
* deuqe(maxlen = size) , 만약 큐사이즈가 꽉찼을때 append가 되면 자동으로 popleft 실행하고 사이즈를 맞춰준다
* deque.remove(value) , del deque[index]

## SET
* set(li) | set(li2) , set(li) & set(li2)
<pre><code>
# 집합 선언
set1 = set([1,2,3])
# 값 하나 추가 
set1.add(4)
# 값 여러개 추가 
set1.update([5,6,7,8,9,10])
# 값 제거 : remove(x)
set1.remove(10)
# 집합 set1 제거
del set1

</code></pre>

## HASH
* dict[key] = dict.get(key,0) + 1
* dict = {} or dict = dict()
* b = dict(a) , copy.deepcopy(a)
* for key, val in dict.items()
* del dict[key]
* sum(dict.values())
<pre><code>
dic = {a :'v', b:'b'}
</code></pre>

## LIST
* del list[index] , list.remove(number)
* deep copy : import copy, copy.deepcopy(list)
* 리스트 리버스 : list.reverse() , list(reversed(List))
* list.count(x) ,list.index(x) < x 없으면 error >
* '@'.join(list)  ex : a@b@c  
* list.count(x)

## HEAP
* import heapq
* heapq.heappop(list)
* heapq.heappush(list, number)
* heapq.heappify(list)

## SORT
 * list = sorted(list, key = lambda x : (x[0], -x[1]))

## STR
* for구문으로 string 다루기 : for X in "abc" => X = a, b, c
* str = "1  "  , str.split(" ") => [1, '', '']  
* str.upper(), str.lower()
* char.isalpha() , char.isdigit() 소수는 flase 나온다.
* string의 첫번째로 나오는 알파벳 대문자 : str.title(), string 맨 앞문자열이 알파벳인 경우 : str.capitalize()
* rjust : "AB".rjust(5,'1') == "111AB"
* replace : "AB".replace('A', '#') == "#B"
* 일치하는 문자열 찾기 : if 'string' in 'Longstring': print('okay')

## FOR
 * for x, y in zip(list1, list2)
 * for i, v in enumerate(list)

## PERMUTATIONS/COMBINATIONS
* form itertools import combinations or permutations
* permutations(list, length) , combinations(list)
* list(set(map(''.join, permutations(list,length))))

## MATH
* import math
* 제곱근 : math.sqrt(num)

## MATRIX
* 전치행렬 : AT = [[ e for e in t ] for t in zip(*A)] 

## 기타
* 타입확인 : type()
* 10진수 2진수로 변환 : bin(x)[2:] (문자의 앞 2개는 ob라서 슬라이싱함)
* m진수 number 10진수로 변환 : int(number, m)
* chr(90) = 'Z' , ord("Z") = 90
* list 안의 내용 유무 확인 : if not list, if list
