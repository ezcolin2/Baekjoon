import sys
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]
dx=[-1, -1, -1, 0, 1, 1, 1, 0] #동서남북 
dy=[-1, 0, 1, 1, 1, 0, -1, -1] #동서남북 
def bfs(a, b): #시작 위치
    if graph[a][b]==1:
        return 0
    arr=[[0]*m for _ in range(n)]
    queue=deque()
    queue.append((a, b))
    visited=[[False]*m for _ in range(n)]
    visited[a][b]=True
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny]==1:
                    return arr[x][y]+1
                queue.append((nx, ny))
                visited[nx][ny]=True
                arr[nx][ny]=arr[x][y]+1
res=0
for i in range(n):
    for j in range(m):
        res=max(res, bfs(i, j))
print(res)