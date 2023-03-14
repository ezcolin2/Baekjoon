import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    subtotal = [0]*(n+1)
    subtotal[0]=0
    for i in range(1, n+1): #누저합 구하기
        subtotal[i]=arr[i-1]
        subtotal[i]+=subtotal[i-1]
    dp=[ 
        [1e9]*n
        for _ in range(n)
    ]
    for i in range(n):
        dp[i][i] = 0 #길이가 1인 것의 최소 비용
    
    for i in range(2, n+1): #길이
        for j in range(n-i+1): #시작 인덱스
            for k in range(j, j+i-1): #하나한씩 돌음
                dp[j][j+i-1] = min(dp[j][j+i-1], dp[j][k]+dp[k+1][j+i-1]+subtotal[j+i]-subtotal[j]) #j+i - j-2 arr[j:j+i]
    print(dp[0][n-1])