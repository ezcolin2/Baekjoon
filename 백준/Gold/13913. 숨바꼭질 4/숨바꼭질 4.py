import sys
from collections import deque
input=sys.stdin.readline
visited=[False]*100001 #방문 여부
from_node=[-1]*100001 #어떤 노드로부터 왔는지
n, k = map(int, input().split())
queue=deque() 
queue.append(n)
visited[n]=True
from_node[n]=-1 #처음 노드는 아무 노드로부터 오지 않았음
while queue: #큐가 빌 때까지
    temp=queue.popleft() #빼기
    if temp==k: #동생을 찾음
        break
    if 0<=temp-1<=100000 and not visited[temp-1]:
        queue.append(temp-1)
        visited[temp-1]=True
        from_node[temp-1]=temp
    if 0<=temp+1<=100000 and not visited[temp+1]:
        queue.append(temp+1)
        visited[temp+1]=True
        from_node[temp+1]=temp
    if 0<=temp*2<=100000 and not visited[temp*2]:
        queue.append(temp*2)
        visited[temp*2]=True
        from_node[temp*2]=temp
cnt=0 #최단 시간
node=k
path=deque([k])
while True: #거꾸로 거슬러 가기
    node=from_node[node] 
    if node==-1: #경로 다 찾음
        break
    path.appendleft(node)
    cnt+=1
print(cnt)
for i in path:
    print(i, end = ' ')