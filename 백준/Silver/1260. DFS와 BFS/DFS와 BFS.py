import sys
from collections import deque
def dfs(k):
    visit[k]=True
    print(k, end=' ')
    for i in range(1, n+1):
        if not visit[i] and connect[k][i]:
            dfs(i)

def bfs(k):
    visit[k]=True
    q=deque([])
    q.append(k)
    while len(q)>0:
        next=q.popleft()
        print(next, end=' ')
        for i in range(1, n+1):
            if not visit[i] and connect[next][i]:
                visit[i]=True
                q.append(i)


n, m, v = map(int, sys.stdin.readline().split())
visit=[False]*(n+1)
connect=[[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    connect[a][b]=True
    connect[b][a]=True
dfs(v)
visit=[False]*(n+1)
print()
bfs(v)

