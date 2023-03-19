import sys
from collections import deque
input=sys.stdin.readline

matrix=[[0]*101 for _ in range(101)]
n=int(input()) #노드 수
m=int(input()) #간선 수
for _ in range(m):
    a, b = map(int, input().split())

    #연결함
    matrix[a][b]=1
    matrix[b][a]=1
visited=[False]*101 #조사했으면 True
q=deque()
cnt=0
def BFS(x): #너비 우선 탐색
    global cnt
    visited[x]=True
    q.append(x)
    while len(q)>0:
        temp=q.popleft() #다음 조사할 노드 
        for i in range(1, n+1):
            if matrix[temp][i]==1 and not visited[i]: #연결되어 있고 아직 조사하지 않았다면 
                visited[i]=True #방문 완료
                
                q.append(i)
                cnt+=1
BFS(1)
print(cnt)
