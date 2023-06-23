import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
MAX=1e9
cost=[
    [MAX]*n
    for _ in range(n)
]
for i in range(n):
    cost[i][i]=0
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1]=min(cost[a-1][b-1], c)
for i in range(n):
    for j in range(n):
        for k in range(n):
            cost[j][k]=min(cost[j][k], cost[j][i]+cost[i][k])
for arr in cost:
    for j in arr:
        if j==MAX:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
