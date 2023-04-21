import sys
from collections import deque
sys.setrecursionlimit(10000)
input=sys.stdin.readline
n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
visited=[[False]*n for _ in range(n)] #방문 여부
corners=set() #모서리 정보 저장. 4방향 조사하다보니 중복이 발생할 수 있어서 set으로 중복 제거
#동서남북
dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
def dfs(x, y, num): #num은 섬의 번호
    visited[x][y]=True
    arr[x][y]=num
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if not (0<=nx<n and 0<=ny<n):
            continue
        if arr[nx][ny]==0: #모서리라면 배열에 넣음
            corners.add((x, y, num))
        if arr[nx][ny]==1 and not visited[nx][ny]:
            dfs(nx, ny, num)
num=2 #섬을 구분하는 식별자
for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and not visited[i][j]:
            dfs(i, j, num)
            num+=1
cnt=1e9 #다리 길이
# print('===============')
# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end=' ')
#     print()
# print('===============')
def bfs(i, j, num): #가장 가까운 섬을 찾는 과정. num은 섬 식별자
    queue=deque()
    queue.append((i, j, 0))
    global cnt
    visited=[[False]*n for _ in range(n)] #방문 여부
    visited[i][j]=True
    while queue: #큐가 빌 때까지
        a, b, c = queue.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if not (0<=nx<n and 0<=ny<n):
                continue
            if arr[nx][ny]!=0 and arr[nx][ny]!=num: #바다가 아니면서 식별자도 다름 = 다른 섬이라는 뜻
                cnt=min(cnt, c) #가장 작은 거리 갱신

            if not visited[nx][ny] and arr[nx][ny]==0: #방문하지 않았고 바다라면 이동
                visited[nx][ny]=True
                queue.append((nx, ny, c+1))
for i in corners:
    a, b, c = i
    bfs(a, b, c)
print(cnt)