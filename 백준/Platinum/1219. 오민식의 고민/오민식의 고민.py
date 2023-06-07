import sys
from collections import deque
input = sys.stdin.readline
INF=1e9
n, start, end, m = map(int, input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))
arr=list(map(int, input().split())) #각 도시에서 벌 수 있는 돈
res=[INF]*n
res[start]=-arr[start]
gee=False #gee 출력 여부
cycle=set() #사이클을 이루고 있는 노드
for i in range(n): #n번 반복
    for from_node, nodes in enumerate(graph):
        for to_node, cost in nodes:
            if res[from_node]!=INF and res[to_node]>res[from_node]+cost-arr[to_node]:
                if i==n-1:
                    gee=True
                    cycle.add(from_node)
                res[to_node]=res[from_node]+cost-arr[to_node]
if res[end]==INF:
    print('gg')
    exit()
while cycle:
    temp=cycle.pop()
    queue=deque()
    queue.append(temp)
    visited=[False]*n
    visited[temp]=True
    while queue:
        node=queue.popleft()
        for to_node, cost in graph[node]:
            if not visited[to_node]:
                queue.append(to_node)
                visited[to_node]=True
    if visited[end]:
        print('Gee')
        exit()
print(-res[end])