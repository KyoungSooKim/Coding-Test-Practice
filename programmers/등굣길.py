def solution(m, n, puddles):
    dis = [[0]*(m+1) for _ in range(n+1)]
    dis[0][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j, i] in puddles:
                continue
            else:
                dis[i][j] = dis[i-1][j] + dis[i][j-1]   
    return dis[n][m]%1000000007