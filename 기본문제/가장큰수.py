from functools import cmp_to_key

def solution(numbers):
    tmp = list(map(str, numbers))
    tmp = sorted(tmp, key=cmp_to_key(compare))
    answer = str(''.join(tmp))
    return answer


def compare(a,b):
    tmp1 = a+b
    tmp2 = b+a
    return (int(tmp1) < int(tmp2)) - (int(tmp1) > int(tmp2))

c = map(int,input().split())
print(solution(c))