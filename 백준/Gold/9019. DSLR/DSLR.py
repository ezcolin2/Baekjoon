from collections import deque
def command_D(number):
    return (number*2)%10000

def command_S(number):
    return 9999 if number == 0 else number-1

def command_L(number):
    return (number*10)%10000 + number//1000

def command_R(number):
    return number//10 + (number%10)*1000

# command를 연결하여 최종 연산 문자열 구하기
def get_full_command(first, goal, command_arr, uf):
    result = []
    while goal != first:
        result.append(command_arr[goal])
        goal = uf[goal]
    return ''.join(result)[::-1]
def get_min_command(first, goal):
    # bfs로 해결
    # command_arr[number] : number가 되기 위해 바로 이전에 적용한 연산
    command_arr = ["" for _ in range(10000)]
    # uf[number] : number가 되기 위해 바로 이전 number
    uf = [i for i in range(10000)]
    visited = [False for _ in range(10000)]
    queue = deque()
    
    # 첫 숫자 방문
    queue.append(first)
    visited[first] = True
    
    # bfs 탐색 시작
    while queue:
        number = queue.popleft()
        if number == goal:
            break
        # 4가지 연산 수행
        new_number = command_D(number)
        if not visited[new_number]:
            visited[new_number] = True
            command_arr[new_number] = "D"
            uf[new_number] = number
            queue.append(new_number)
        new_number = command_S(number)
        if not visited[new_number]:
            visited[new_number] = True
            command_arr[new_number] = "S"
            uf[new_number] = number
            queue.append(new_number)
        new_number = command_L(number)
        if not visited[new_number]:
            visited[new_number] = True
            command_arr[new_number] = "L"
            uf[new_number] = number
            queue.append(new_number)
        new_number = command_R(number)
        if not visited[new_number]:
            visited[new_number] = True
            command_arr[new_number] = "R"
            uf[new_number] = number
            queue.append(new_number)
    return get_full_command(first, goal, command_arr, uf)

t = int(input())
for _ in range(t):
    first, goal = map(int, input().split())
    print(get_min_command(first, goal))