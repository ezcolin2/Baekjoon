from collections import deque
def command_D(number):
    return (number*2)%10000

def command_S(number):
    return 9999 if number == 0 else number-1

def command_L(number):
    return (number*10)%10000 + number//1000

def command_R(number):
    return number//10 + (number%10)*1000

def get_min_command(first, goal):
    # bfs로 해결
    commands_arr = ["" for _ in range(10000)]
    visited = [False for _ in range(10000)]
    queue = deque()
    
    # 첫 숫자 방문
    queue.append(first)
    visited[first] = True
    
    # bfs 탐색 시작
    while queue:
        number = queue.popleft()
        if number == goal:
            return commands_arr[goal]
        # 4가지 연산 수행
        new_number = command_D(number)
        if not visited[new_number]:
            visited[new_number] = True
            commands_arr[new_number] = commands_arr[number]+"D"
            queue.append(new_number)
        new_number = command_S(number)
        if not visited[new_number]:
            visited[new_number] = True
            commands_arr[new_number] = commands_arr[number]+"S"
            queue.append(new_number)
        new_number = command_L(number)
        if not visited[new_number]:
            visited[new_number] = True
            commands_arr[new_number] = commands_arr[number]+"L"
            queue.append(new_number)
        new_number = command_R(number)
        if not visited[new_number]:
            visited[new_number] = True
            commands_arr[new_number] = commands_arr[number]+"R"
            queue.append(new_number)
    return commands_arr[goal]

t = int(input())
for _ in range(t):
    first, goal = map(int, input().split())
    print(get_min_command(first, goal))