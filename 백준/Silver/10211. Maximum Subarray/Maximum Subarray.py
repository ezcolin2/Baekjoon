import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[-1e9]+list(map(int, input().split()))
    for i in range(1, n+1):
        arr[i]=max(arr[i], arr[i-1]+arr[i])
    print(max(arr))