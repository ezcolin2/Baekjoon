import sys
input=sys.stdin.readline
INF=1e9
n, k = map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
# 플로이드 와샬 알고리즘
distance=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i]=0
for row, arr in enumerate(graph):
    for col in arr:
        distance[row][col]=1
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            distance[a][b]=min(distance[a][b], distance[a][i]+distance[i][b])
s=int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if distance[a][b]!=INF and distance[a][b]>0:
        print(-1)
    elif distance[b][a]!=INF and distance[b][a]>0:
        print(1)
    else:
        print(0)