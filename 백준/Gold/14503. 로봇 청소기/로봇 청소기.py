# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 반시계 방향으로 돌 때 
rotate_counter_clock_wise = {
    0: 3,
    1: 0,
    2: 1,
    3: 2
}

# 뒤로 돌 때 
rotate_backward = {
    0: 2,
    1: 3,
    2: 0,
    3: 1
}

# 현재 위치 주위 4칸이 청소되었는지
def is_cleaned_around(arr, cleaned, x, y):
    n = len(arr)
    m = len(arr[0])
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위를 벗어나거나 벽이면 스킵
        if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == 1:
            continue
        # 만약 청소되지 않은 칸이 있다면 False 반환
        if not cleaned[nx][ny]:
            return False
    return True 

# 청소된 영역의 개수 반환
def get_cleaned_cnt(cleaned):
    return sum([row.count(True) for row in cleaned])

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def solution():
    cleaned = [[False]*m for _ in range(n)]
    curr_x, curr_y, curr_d = r, c, d
    while True:
        # 현재 칸이 청소되지 않은 경우 청소
        if not cleaned[curr_x][curr_y]:
            cleaned[curr_x][curr_y] = True
        
        # 현재 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if is_cleaned_around(arr, cleaned, curr_x, curr_y):
            # 뒤로 이동할 때 좌표 
            next_direction = rotate_backward[curr_d]
            nx, ny = curr_x + dx[next_direction], curr_y + dy[next_direction]
            
            # 뒤로 이동할 수 있다면 후진
            if 0<= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                # 위치만 뒤로 가고 방향은 갱신하지 않는다.
                curr_x, curr_y = nx, ny 
                # 1번으로 돌아간다.
                continue
            # 뒤로갈 수 없다면 멈춘다.
            return get_cleaned_cnt(cleaned)
        # 현재 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        # 위치를 반시계 방향으로 갱신한다.
        curr_d = rotate_counter_clock_wise[curr_d]
        # 앞 위치를 구한다.
        nx, ny = curr_x + dx[curr_d], curr_y + dy[curr_d]
        
        # 청소되지 않았다면 전진
        if 0<= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and not cleaned[nx][ny]:
            # 위치 갱신
            curr_x, curr_y = nx, ny
print(solution())