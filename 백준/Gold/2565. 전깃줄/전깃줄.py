import sys
n=int(sys.stdin.readline())
li=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
li.sort()
li=[i[1] for i in li]
dp=[0]*501
dp[li[0]]=1
for i in li:
    dp[i]=max(dp[:i])+1


print(n-max(dp))