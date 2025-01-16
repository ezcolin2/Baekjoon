
from collections import deque
# 동서남북
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# 벽을 한 개까지 부수고 이동할 수 있다는 제한이 있다.
# 최단 거리만 고려하다가 마지막 벽에 가로막혀 이동할 수 없는 상황을 방지해야 한다.
# 방문 배열에 벽을 부쉈는지 체크하는 차원을 추가한다.
def bfs(arr, start_x, start_y):
    n, m = len(arr), len(arr[0])
    # visited[i][j][k]의 의미 : 좌표 (i, j)에 벽을 부술 수 있는 횟수가 k번 남도록 방문 여부
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    distance = [[[0, 0] for _ in range(m)] for _ in range(n)]
    
    # 초기 값 세팅
    queue = deque([(start_x, start_y, 1)])
    
    visited[start_x][start_y][1] = True
    distance[start_x][start_y][1] = 1
    
    # bfs 탐색 시작
    while queue:
        x, y, remain = queue.popleft()
        
        # 4방향 탐색
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            # 좌표 벗어나는지 확인
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            # 벽을 부술 수 없음
            if remain == 0:
                # 벽이 있다면
                if not visited[nx][ny][1] and arr[nx][ny] == 1:
                    visited[nx][ny][1] = True
                # 벽이 없다면
                if not visited[nx][ny][0] and arr[nx][ny] == 0:
                    visited[nx][ny][0] = True
                    distance[nx][ny][0] = distance[x][y][0]+1
                    queue.append((nx, ny, 0))
            # 벽을 부술 수 있음
            else:
                # 벽이 있다면
                if not visited[nx][ny][0] and arr[nx][ny] == 1:
                    visited[nx][ny][0] = True
                    distance[nx][ny][0] = distance[x][y][1]+1
                    queue.append((nx, ny, 0))
                # 벽이 없다면
                if not visited[nx][ny][1] and arr[nx][ny] == 0:
                    visited[nx][ny][1]= True
                    distance[nx][ny][1] = distance[x][y][1]+1
                    queue.append((nx, ny, 1))
                    
    filtered = list(filter(lambda x:x!=0, distance[-1][-1]))
    if len(filtered) == 0:
        return -1
    return min(filtered)
            
n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
print(bfs(arr, 0, 0))