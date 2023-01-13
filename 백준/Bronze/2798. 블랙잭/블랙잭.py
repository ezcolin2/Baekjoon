import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
res=0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp=li[i]+li[j]+li[k]
            if temp>m:
                continue
            else:
                res=max(res,temp)
print(res)