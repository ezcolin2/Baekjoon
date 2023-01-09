li=list(map(int,input()))
if li[0]==0:
    print(0)
    exit()
size=len(li)
dp=[0]*(size+1)

dp[0]=1
dp[1]=1
for i in range(1, size):
    if li[i-1]==1:
        if li[i]==0:
            dp[i+1]=dp[i-1]
        else:
            dp[i+1]=dp[i-1]+dp[i]
    elif li[i-1]==2:
        if li[i]==0:
            dp[i+1]=dp[i-1]
        elif 1<=li[i]<=6:
            dp[i+1]=dp[i-1]+dp[i]
        else:
            dp[i+1]=dp[i]
    else:
        if li[i]==0:
            print(0)
            exit()
        dp[i+1]=dp[i]
print(dp[size]%1000000)