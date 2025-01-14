from collections import deque
# 동서남북
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# start_x, start_y부터 bfs 탐색 시작
def bfs(arr, visited, start_x, start_y):
    n = len(arr)
    m = len(arr[0])
    # 큐에 초기 좌표 삽입
    queue = deque([(start_x, start_y)])
    
    # 큐가 빌 때까지
    while queue:
        # 빼기
        current_x, current_y = queue.popleft()
        visited[current_x][current_y] = True
        
        # 4방향을 보면서 조건 확인
        for i in range(4):
            next_x, next_y = current_x+dx[i], current_y+dy[i] 
            
            # 배열을 벗어나면 스킵   
            if next_x<0 or next_x>=n or next_y<0 or next_y>=m:
                continue
            
            # 방문했다면 스킵
            if visited[next_x][next_y]:
                continue
            
            # 배추가 없다면 스킵
            if arr[next_x][next_y] == 0:
                continue
            
            # 범위 안에 있고 방문하지 않았고 배추가 있다면 큐에 넣기
            queue.append((next_x, next_y))
            visited[next_x][next_y] = True

# 지렁이 개수
def get_number_of_jireong(arr):
    n = len(arr)
    m = len(arr[0])
    res = 0
    visited = [[False]*m for _ in range(n)]
    
    # 방문하지 않았고 배추가 있는 곳을 찾는다.
    for i in range(n):
        for j in range(m):
            # 방문했거나 배추가 없으면 스킵
            if visited[i][j] or arr[i][j] == 0:
                continue
                
            # 탐색 시작
            bfs(arr, visited, i, j)
            res+=1
    return res
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
    print(get_number_of_jireong(arr))
            
                