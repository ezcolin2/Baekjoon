from collections import deque
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# bfs
def bfs(arr):
    area_arr = []
    n, m = len(arr), len(arr[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 모든 점에 대해서 시작하기
    for i in range(n):
        for j in range(m):
            # 만약 직사각형이 그려져 있거나 방문했다면 스킵
            if arr[i][j] == 1 or visited[i][j]:
                continue
            
            # 방문하기
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            area = 1
            
            # 큐가 빌 때까지
            while queue:
                x, y = queue.popleft()
                # 4방향 탐색
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    # 범위 벗어나면 스킵
                    if nx<0 or nx>=n or ny<0 or ny>=m:
                        continue
                        
                    # 이미 방문했거나 직사각형이 그려져 있으면 스킵
                    if arr[nx][ny] == 1 or visited[nx][ny]:
                        continue
                    
                    # 방문
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    area+=1
            area_arr.append(area)
    return area_arr
m, n, k = map(int, input().split())
# 직사각형을 1로 표현 
arr = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(x1, x2):
        for x in range(y1, y2):
            arr[x][y] = 1

# 각 영역 별 넓이 배열

area_arr = bfs(arr)
area_arr.sort()
print(len(area_arr))
for area in area_arr:
    print(area, end=' ')                
            