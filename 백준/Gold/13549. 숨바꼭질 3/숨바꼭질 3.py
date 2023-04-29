import sys
from collections import deque
input=sys.stdin.readline
n, k = map(int, input().split())
visited=[False]*100001
cnt=[0]*100001
def bfs(n):
    queue=deque()
    queue.append(n)
    visited[n]=True
    while queue:
        temp=queue.popleft()
        if temp==k: #찾았다면
            print(cnt[temp])
            exit()
        #방문하지 않았고 갈 수 있다면 추가
        if 0<=temp*2<=100000 and not visited[temp*2]:
            queue.appendleft(temp*2) 
            cnt[temp*2]=cnt[temp]
            visited[temp*2]=True
        if 0<=temp-1<=100000 and not visited[temp-1] :
            queue.append(temp-1)
            cnt[temp-1]=cnt[temp]+1
            visited[temp-1]=True
        if 0<=temp+1<=100000 and not visited[temp+1] :
            queue.append(temp+1) 
            cnt[temp+1]=cnt[temp]+1
            visited[temp+1]=True
bfs(n)