import sys
input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
dx = [0, 0, 1, -1] # 동서남북
dy = [1, -1, 0, 0] # 동서남북
s = set() # 방문한 알파벳 집합
s.add(arr[0][0])
res=0
def dfs(x, y, n):
    global res
    res=max(res, n)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<r and 0<=ny<c and arr[nx][ny] not in s:
            s.add(arr[nx][ny])
            dfs(nx, ny, n+1)
            s.remove(arr[nx][ny])
dfs(0, 0, 1)
print(res)