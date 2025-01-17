from collections import deque
import sys
MAX_VALUE = sys.maxsize
# 동서남북
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs_water(arr):
    n, m = len(arr), len(arr[0])
    
    # 방문 여부 
    water_visited = [[False for _ in range(m)] for _ in range(n)]
    
    # 최단 거리
    water_distance = [[MAX_VALUE for _ in range(m)] for _ in range(n)]
    
    # 큐
    queue = deque()
    
    # 물의 위치를 초기화한다.
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                queue.append((i, j))
                water_visited[i][j] = True
                water_distance[i][j] = 0
    
    # 물부터 최단 거리를 구한다.
    while queue:
        x, y = queue.popleft()
        
        # 4방향 탐색
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            # 범위 벗어난다면 스킵
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            # 돌이거나 비버 굴이라면 스킵
            if arr[nx][ny] == 'X' or arr[nx][ny] == 'D':
                continue
            
            
            # 방문했다면 스킵
            if water_visited[nx][ny]:
                continue
            
            
            # 방문한다.
            queue.append((nx, ny))
            water_visited[nx][ny] = True
            water_distance[nx][ny] = water_distance[x][y]+1
    return water_distance
    
def bfs_animal(arr, water_distance):
    n, m = len(arr), len(arr[0])
    
    # 방문 여부 
    animal_visited = [[False for _ in range(m)] for _ in range(n)]
    
    # 최단 거리
    animal_distance = [[0 for _ in range(m)] for _ in range(n)]
    
    # 큐
    queue = deque()
            
    # 고슴도치의 위치를 초기화한다.
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'S':
                queue.append((i, j))
                animal_visited[i][j] = True
    
    # 고슴도치의 최단 거리를 구한다.
    while queue:
        x, y = queue.popleft()
        
        # 4방향 탐색
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            # 범위 벗어난다면 스킵
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            # 돌이라면 스킵
            if arr[nx][ny] == 'X':
                continue
            
            # 방문했다면 스킵
            if animal_visited[nx][ny]:
                continue
            
            # 물이 찰 예정이라면 스킵
            if water_distance[nx][ny] <= animal_distance[x][y]+1:
                continue
            
            # 방문한다.
            queue.append((nx, ny))
            animal_visited[nx][ny] = True
            animal_distance[nx][ny] = animal_distance[x][y]+1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'D':
                return animal_distance[i][j]
        
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
water_distance = bfs_water(arr)
res = bfs_animal(arr, water_distance)
print(res if res != 0 else 'KAKTUS')