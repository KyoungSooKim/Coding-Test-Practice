answer = 0
def solution(numbers, target):
    length = len(numbers) 
    tal = sum(numbers)
    def DFS(L, sum, leftSum, ):
        global answer
        # if (leftSum + sum) < target:
        #     return
        # if sum > target and (sum - leftSum) > target:
        #     return
        if L == length:
            if sum == target:
                answer += 1
            return
        else:
            DFS(L+1, sum + numbers[L], leftSum -  numbers[L])
            DFS(L+1, sum - numbers[L], leftSum -  numbers[L])      
    DFS(0,0,tal)
    return answer