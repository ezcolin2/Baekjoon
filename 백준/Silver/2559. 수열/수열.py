import sys
n, m = map(int, sys.stdin.readline().split())
li=list(map(int, sys.stdin.readline().split()))
li.insert(0, 0)
for i in range(1, n+1):
    li[i]+=li[i-1]
res=-1e9
for i in range(m, n+1):
    res=max(res, li[i]-li[i-m])
print(res)