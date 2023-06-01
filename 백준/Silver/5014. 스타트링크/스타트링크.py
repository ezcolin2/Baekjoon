import sys
from collections import deque
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
queue=deque()
visited=[False]*(f+1) #해당 층수 방문 여부
arr=[0]*(f+1) #이동 횟수
queue.append(s)
visited[s]=True
arr[s]=0
while queue: #큐가 빌 때까지
    temp=queue.popleft() #하나 빼기
    if temp==g: #목적지에 도착하면 끝 
        print(arr[temp])
        exit()
    if 1<=temp+u<=f and not visited[temp+u]:
        queue.append(temp+u)
        visited[temp+u]=True
        arr[temp+u]=arr[temp]+1
    if 1<=temp-d<=f and not visited[temp-d]:
        queue.append(temp-d)
        visited[temp-d]=True
        arr[temp-d]=arr[temp]+1
#반복문을 빠져나왔다는 것은 갈 수 없다는 뜻 
print("use the stairs")