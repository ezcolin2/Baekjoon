import sys
input=sys.stdin.readline
n, m = map(int, input().split())
arr=[]
parents=[i for i in range(n+1)]
def parent(a):
    if parents[a]==a:
        return a
    return parent(parents[a])
for _ in range(m):
    u, v, w = map(int, input().split())
    arr.append((w, u, v))
arr.sort()
res=0
last=0
for i in arr:
    if parent(i[1])!=parent(i[2]):
        a=parent(i[1])
        b=parent(i[2])
        if a<b:
            parents[b]=a
        else:
            parents[a]=b
        res+=i[0]
        last=i[0]
print(res-last)