import sys
from collections import deque
input = sys.stdin.readline
dx=[-2, -2, 0, 0, 2, 2]
dy=[-1, 1, -2, 2, -1, 1]
n=int(input())
visited=[[False]*n for _ in range(n)] #방문 여부
arr=[[0]*n for _ in range(n)] #이동 횟수
def can_go(r, c): # (r,c)에 갈 수 있는지 여부
    return 0<=r<n and 0<=c<n and not visited[r][c]
r1, c1, r2, c2=list(map(int, input().split()))
q = deque()
q.append([r1, c1])
visited[r1][c1]=True
while q: #큐가 빌 때까지
    temp=q.popleft() #하나 꺼냄
    for i in range(6):
        temp_r=temp[0]+dx[i]
        temp_c=temp[1]+dy[i]
        if can_go(temp_r, temp_c): #갈 수 있다면
            if temp_r==r2 and temp_c==c2: #도착
                print(arr[temp[0]][temp[1]]+1)
                exit()
            visited[temp_r][temp_c]=True #갔다고 표시
            arr[temp_r][temp_c]=arr[temp[0]][temp[1]]+1
            q.append([temp_r, temp_c]) #큐에 넣음
#반복문이 끝나면 도착할 수 없는 것 
print(-1)