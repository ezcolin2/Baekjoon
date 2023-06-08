import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph=[[0]*(n+1)]+[[0]+list(map(int, input().rstrip())) for _ in range(m)]
visited=[[False]*(n+1) for _ in range(m+1)] #방문 여부 
arr=[[0]*(n+1) for _ in range(m+1)] #부순 벽 개수
dx=[0, 0, 1, -1] #동서남북
dy=[1, -1, 0, 0] #동서남북
queue=deque()
queue.append((1, 1))
visited[1][1]=True
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 1<=nx<=m and 1<=ny<=n and not visited[nx][ny]:
            arr[nx][ny]=arr[x][y]+graph[nx][ny] #벽이 있으면 1추가
            visited[nx][ny]=True
            if graph[nx][ny]==1: #벽이 있다면
                queue.append((nx, ny)) #뒤에 넣기
            else:
                queue.appendleft((nx, ny)) #앞에 넣기
print(arr[m][n])