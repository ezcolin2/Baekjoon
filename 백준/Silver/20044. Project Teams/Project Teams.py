import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int, input().split()))
arr.sort()
res=1e9
for i in range(n):
    res=min(res, arr[i]+arr[-i-1])
print(res)
