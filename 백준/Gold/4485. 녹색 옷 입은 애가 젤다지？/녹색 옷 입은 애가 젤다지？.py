
import sys
import heapq
input=sys.stdin.readline
MAX=1e9
dx=[0, 0, 1, -1] #동서남북 
dy=[1, -1, 0, 0] #동서남북 
def can_go(a, b, n): #n*n에서 [a][b] 갈 수 있는지
    return 0<=a<n and 0<=b<n
cnt=0
while True:
    n=int(input())
    cnt+=1
    if n==0:
        break
    arr=[
        list(map(int, input().split())) 
        for  _ in range(n)
    ]
    arr2=[
        [MAX]*(n)
        for _ in range(n)
    ]
    visited=[
        [False]*(n)
        for _ in range(n)
    ]
    queue = [] #최소 힙
    #참고로 마지막에 arr[0][0] 더하는 거 잊지 말기
    heapq.heappush(queue, (0, (0, 0))) #금액과 위치
    while queue:
        cost, coordinate = heapq.heappop(queue) #금액과 위치 빼옴
        for i in range(4): #동서남북 조사
            nx=coordinate[0]+dx[i]
            ny=coordinate[1]+dy[i]
            if can_go(nx, ny, n) and not visited[nx][ny]: #좌표를 벗어나지 않는다면
                heapq.heappush(queue, (cost+arr[nx][ny], (nx, ny)))
                arr2[nx][ny]=cost+arr[nx][ny]
                visited[nx][ny]=True
    print(f"Problem {cnt}: {arr2[n-1][n-1]+arr[0][0]}")
