import sys
from collections import deque
input=sys.stdin.readline
MAX=1e9
def fordFulkerson(graph, s, t, n): 
    #graph는 그래프. 간선의 비용 정보
    #s는 시작 노드
    #t는 도착 노드 
    #n은 노드의 개수
    remain=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            remain[i][j]=graph[i][j]
    max_flow=0 #최대 유량
    while True:
        #bfs 시작 
        ####################################
        visited=[False]*n
        queue=deque()
        queue.append(s)
        visited[s]=True
        path=[-1]*n #경로. 부모 노드를 저장. 거슬러 올라가면 경로 구할 수 있음
        path[s]=-1 #처음 노드는 부모 노드가 없음
        while queue:
            a=queue.popleft()
            for b in range(n):
                if not visited[b] and remain[a][b]>0: #방문하지 않았고 갈 수 있다면
                    queue.append(b)
                    path[b]=a #부모 노드 저장
                    visited[b]=True
        if not visited[t]: #목적지로 가는 경로가 없다면
            break
        #bfs 끝. 경로는 도착 노드인 t 부터 path를 보면서 부모 노드를 거슬러 올라가면 됨
        #####################################


        b=t #경로를 거슬러 올라가기 위한 변수
        min_remain=MAX #경로 간선들 중 가장 작은 용량을 구하기 위한 변수
        while b!=s: #처음 노드에 도착할 때까지
            a=path[b]
            min_remain=min(min_remain, remain[a][b]) 
            b=a
            
        b=t
        while b!=s:
            a=path[b]
            remain[a][b]-=min_remain
            remain[b][a]+=min_remain
            b=a
        max_flow+=min_remain
    return max_flow


graph=[[0]*52 for _ in range(52)] #소문자 + 대문자 = 52
n=int(input())
for _ in range(n):
    a, b, c = input().split()
    c=int(c)
    a=ord(a)-ord('a') if a.islower() else ord(a)-ord('A')+26
    b=ord(b)-ord('a') if b.islower() else ord(b)-ord('A')+26
    graph[a][b]+=c
    graph[b][a]+=c
print(fordFulkerson(graph, 26, 51, 52))