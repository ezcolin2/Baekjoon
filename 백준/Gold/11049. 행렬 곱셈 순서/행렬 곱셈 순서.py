import sys
input=sys.stdin.readline
n=int(input())
arr=[tuple(map(int, input().split())) for _ in range(n)]
dp=[[0]*501 for _ in range(501)]
for i in range(n):
    dp[i][i]=0
for i in range(n-1):
    dp[i][i+1]=arr[i][0]*arr[i+1][0]*arr[i+1][1]
for i in range(1, n): #부분 배열 길이
    for j in range(n-i): #시작 위치 
        dp[j][j+i]= 1e9
        for k in range(j, j+i+1): #부분 배열의 끝?
            dp[j][j+i]=min(dp[j][j+i], dp[j][k]+dp[k+1][j+i]+arr[j][0]*arr[k][1]*arr[j+i][1])
print(dp[0][n-1])