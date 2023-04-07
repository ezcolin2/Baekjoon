import sys
input=sys.stdin.readline
n, m = map(int, input().split())
arr=[list(input().rstrip()) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]
def DFS(si, sj, i, j, color, cnt): #si, sj는 시작 좌표. i, j는 현재 좌표
    for k in range(4):
        ni=i+dy[k]
        nj=j+dx[k]
        if 0<=ni<n and 0<=nj<m:
            if visited[ni][nj]==True and arr[ni][nj]==color and ni==si and nj==sj and cnt>=4:
                print('Yes')
                exit()
            elif visited[ni][nj]==False and arr[ni][nj]==color: #방문하지 않았고 색깔이 같으면
                visited[ni][nj]=True
                DFS(si, sj, ni, nj, arr[ni][nj], cnt+1)
                visited[ni][nj]=False
for i in range(n):
    for j in range(m):
        if visited[i][j]==False: #아직 방문하지 않았다면
            visited[i][j]=True
            DFS(i, j, i, j, arr[i][j],1)
            visited[i][j]=False
print('No')
