import sys
from collections import deque
input=sys.stdin.readline
def can_visit(n, m): #(n, m)을 방문할 수 있는지 
    return 0<=n<l and 0<=m<l
def BFS(n, m, l, ea, eb):
    q=deque()
    q.append((n, m)) #시작 위치 넣기
    visited[n][m]=True
    arr=[[0]*l for _ in range(l)]
    while len(q)>0: #큐가 빌 때까지 반복
        temp=q.popleft()
        x=temp[1]
        y=temp[0]
        if x==eb and y==ea:
            return arr[y][x]
        for i in range(8): #8방향 전부 조사
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l and not visited[ny][nx]: #아직 방문하지 않았고 갈 수 있다면
                q.append((ny, nx))
                visited[ny][nx]=True
                arr[ny][nx]=arr[y][x]+1
dx=[1, 2, 2, 1, -1, -2, -2, -1]
dy=[2, 1, -1, -2, -2, -1, 1, 2]
n=int(input())
for _ in range(n):
    l=int(input())
    visited=[[False]*l for _ in range(l)] #방문 여부
    sa, sb = map(int, input().split())
    ea, eb = map(int, input().split())
    res=BFS(sa, sb, l, ea, eb)
    print(res)
