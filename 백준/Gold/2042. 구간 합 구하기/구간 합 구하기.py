import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr=[0]*(n+1)
tree=[0]*(n+1)
def update(i, num):
    arr[i]+=num
    while i<=n:
        tree[i]+=num
        i+=i&-i
def sum(i):
    res=0
    while i>0:
        res+=tree[i]
        i-=i&-i
    return res
for i in range(1, n+1):
    update(i, int(input()))
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a==1:
        update(b, c-arr[b])
    else:
        print(sum(c)-sum(b-1))