import sys
n, m = map(int, sys.stdin.readline().split())
li=list(map(int, sys.stdin.readline().split()))
li.insert(0, 0)
for i in range(1, n+1):
    li[i]+=li[i-1]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(li[b]-li[a-1])