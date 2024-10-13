# 이동 제한
# 1. 자신의 크기보다 큰 물고기는 지나갈 수 없다. (크기가 같은 물고기는 이동만 가능)
# 2. 상->좌->우->하 순서대로 bfs를 진행한다.

# 필요 변수
# 1. 상어의 크기
# 2. 상어가 잡아먹은 물고기의 개수 (1번과 같아지면 0으로 초기화)

from collections import deque
# 상좌우하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
# 좌표를 벗어나는지
def is_possible_range(n, x, y):
    return 0<=x<n and 0<=y<n

# 이동할 수 있는지
# 무조건 is_possible_range 실행 후 실행한다.
def can_move(shark_size, arr, nx, ny):
    return shark_size >= arr[nx][ny]

# 먹을 수 있는지
# 무조건 is_possible_range 실행 후 실행한다.
def can_eat(shark_size, arr, nx, ny):
    return arr[nx][ny] !=0 and arr[nx][ny] != 9 and shark_size > arr[nx][ny]

# 상어의 다음 위치와 거리 찾기
# 만약 제자리라면 더이상 먹을 수 있는 물고기가 없다는 뜻이다. 
def get_next_location_and_distance(shark_size, arr, x, y):
    n = len(arr)
    # 방문 여부
    visited = [[False]*n for _ in range(n)]
    
    # 초기 위치 방문
    visited[x][y] = True
    queue = deque([(x, y, 0)])
    
    # 먹을 수 있는 물고기 위치 배열
    fishes = []
    
    # bfs 시작
    while queue:
        current_x, current_y, current_distance = queue.popleft()
        # 만약 현재 위치가 먹을 수 있는 물고기 위치라면 현재 위치 반환
        if can_eat(shark_size, arr, current_x, current_y):
            # 가장 짧은 거리 -> 가장 위 -> 가장 왼쪽 순서
            fishes.append((current_distance, current_x, current_y))
            continue
        
        # 상좌하우 탐색
        for i in range(4):
            # 다음 위치
            nx, ny = current_x+dx[i], current_y+dy[i]
            # 만약 범위를 벗어나면 스킵
            if not is_possible_range(n, nx, ny):
                continue 
            
            # 이동 가능하다면 이동
            if not visited[nx][ny] and can_move(shark_size, arr, nx, ny):
                visited[nx][ny] = True
                queue.append((nx ,ny, current_distance + 1))
    if len(fishes) == 0:
        return x, y, 0
    fishes.sort()
    return fishes[0][1], fishes[0][2], fishes[0][0]

# 초기 상어 위치를 반환한다.
def get_shark_loation(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                return i, j
def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    shark_size = 2 # 상어의 크기
    fish_count = 0 # 상어가 먹은 물고기 개수
    time = 0 # 시간
    x, y = get_shark_loation(arr) # 상어 초기 위치
    arr[x][y] = 0 # 상어 위치를 0으로 만든다.
    
    # 더이상 먹을 물고기가 없을 때까지 반복한다.
    while True:
        # 다음 위치
        nx, ny, distance = get_next_location_and_distance(shark_size, arr, x, y)
        # 만약 현재 위치와 같다는 뜻은 더이상 먹을 물고기가 없다는 뜻이다.
        if x == nx and y == ny and distance == 0:
            return time
        
        # 먹을 물고기를 찾았다면 재방문하지 않게 0으로 초기화
        arr[nx][ny] = 0
        x, y = nx, ny # 갱신
        time += distance # 시간 증가
        fish_count += 1 # 먹은 물고기 개수 증가
        
        # 만약 현재 크기와 물고기 개수가 같다면 크기 증가 물고기 개수 초기화
        if shark_size == fish_count:
            shark_size += 1
            fish_count = 0
        
res = solution()
print(res)