# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, east, west, south, north = map(int, input().split())
dpercent = [east/100, west/100, south/100, north/100]
total_percent = 0
visited = [[False for _ in range(32)] for _ in range(32)]
def DFS(count, x, y, current_percent):
    global total_percent
    if count == n+1:
        total_percent += current_percent
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        DFS(count+1, nx, ny, current_percent*dpercent[i])
        visited[nx][ny] = False
DFS(0, 15, 15, 1)
print(total_percent)