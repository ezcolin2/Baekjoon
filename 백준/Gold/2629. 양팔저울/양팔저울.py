import sys
input=sys.stdin.readline
n=int(input()) #추의 개수
chu=list(map(int, input().split()))
m=int(input()) #확인할 무게의 개수
weights=list(map(int, input().split()))
dp=[[False]*40001 for _ in range(n+1)] #dp[x][y]는 x번째까지 추로 무게 y를 만들 수 있는지
dp[0][0]=True
for i in range(1, n+1):
    weight = chu[i-1]
    for j in range(15001):
        if dp[i-1][j] or dp[i-1][abs(j-weight)] or dp[i-1][j+weight]:
            dp[i][j]=True
for i in weights:
    if dp[n][i]:
        print('Y', end=' ')
    else:
        print('N', end=' ')
