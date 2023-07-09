import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
arr=[deque(input().rstrip()) for _ in range(t)]
#rotation 값이 1이면 시계 방향 회전, 0이면 반시계 방향 회전, -1이면 회전하지 않음.
def is_turn_right(rotation, queue): 
    if rotation==1:
        last=queue.pop()
        queue.appendleft(last)
    elif rotation==0:
        last=queue.popleft()
        queue.append(last)
    

k=int(input())
for _ in range(k):
    num, direction = map(int, input().split())
    num-=1 # 인덱스 맞추기 위함
    temp=[-1 for _ in range(t)] # 회전 방향
    temp[num] = 1 if direction==1 else 0 # direction이 1이면 시계 방향. 아니면 반시계 방향.



    # 오른쪽부터 조사. 극이 같다면 회전 x. 다르면 다른 방향 회전.
    for i in range(num+1, t):
        if arr[i-1][2]==arr[i][6]:
            temp[i]=-1
        elif temp[i-1]==1:
            temp[i]=0
        elif temp[i-1]==0:
            temp[i]=1
        else:
            temp[i]=-1

    # 왼쪽 조사. 극이 같다면 회전 x. 다르면 다른 방향 회전.
    for i in range(num-1, -1, -1):
        if arr[i+1][6]==arr[i][2]:
            temp[i]=-1
        elif temp[i+1]==1:
            temp[i]=0
        elif temp[i+1]==0:
            temp[i]=1
        else:
            temp[i]=-1

    for i in range(t): # 나머지 모든 톱니바퀴 회전
        is_turn_right(temp[i], arr[i])
cnt=0 # s극 개수
for queue in arr:
    if queue.popleft()=='1':
        cnt+=1
print(cnt)