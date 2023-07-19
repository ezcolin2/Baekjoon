# 백준 2589
# bfs
import sys
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split())
arr=[list(input().rstrip()) for _ in range(n)]
dx=[0, 0, 1, -1] # 동서남북
dy=[1, -1, 0, 0] # 동서남북
visited=[]
def can_visit(a, b): # (a, b) 좌표 방문 가능 여부
    return 0<=a<n and 0<=b<m and not visited[a][b] and arr[a][b]=='L'
def bfs(a, b): # (a, b) 좌표부터 탐색 시작 
    global visited
    visited=[[False]*m for _ in range(n)]
    distance=[[0]*m for _ in range(n)]
    queue=deque() # 큐
    if not can_visit(a, b): # 방문할 수 없다면 0 반환 
        return 0
    queue.append((a, b))
    visited[a][b]=True
    res=0 # 가장 긴 최단 거리
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if can_visit(nx, ny): # 방문 가능하면 방문
                distance[nx][ny]=distance[x][y]+1
                res=max(res, distance[nx][ny])
                visited[nx][ny]=True
                queue.append((nx, ny))
    return res
res=0
for i in range(n):
    for j in range(m):
        res=max(res, bfs(i, j))
print(res)
