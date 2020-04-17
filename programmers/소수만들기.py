from itertools import combinations
import math

def isPrime(num):
    if num == 1: return False
    
    n = int(math.sqrt(num))
    
    for x in range(2,n+1):
        if num%x == 0: return False
    else:
        return True

def solution(nums):
    answer = 0

    tmp = list(combinations(nums, 3))
    for x in tmp:
        if isPrime(sum(x)): answer += 1
        
    return answer