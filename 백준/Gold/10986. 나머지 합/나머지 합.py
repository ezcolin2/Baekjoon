import sys
n, m = map(int, sys.stdin.readline().split())
li=list(map(int, sys.stdin.readline().split()))
li.insert(0,0)
acc=[0]*(n+1)
mod=[0]*m
mod[0]=1
for i in range(1, n+1):
    li[i]+=li[i-1]
    acc[i]=li[i]%m
    mod[acc[i]]+=1
res=0
for i in range(m):
    res+=(mod[i]*(mod[i]-1))//2
print(res)