import sys
from collections import defaultdict
input=sys.stdin.readline
S=input().rstrip()
n=int(input())
A=[input().rstrip() for _ in range(n)]
#graph[i]==j의 의미는 S[i:j+1]이 A에 포함된다는 뜻
# graph=[[] for _ in range(len(S)+1)]
graph=defaultdict(lambda : []) 
def make_graph(x): # A에 속한 문자열 x가 S에 포함되면 그래프 생성
    for i in range(len(S)-len(x)+1):
        if S[i:i+len(x)]==x: # 포함된다면
            graph[i].append(i+len(x)) # 끝 칸 하나 늘려서 저장
for i in A:
    make_graph(i)
#그래프가 완성됐으니 dfs 시작
visited=[False]*(len(S)+1) # 노드 방문 여부
start_node=0 # 출발 노드
end_node=len(S) # 도착 노드
def dfs(x):
    visited[x]=True
    if x==end_node: # 목적지에 도착했다면
        print(1)
        exit()
    for i in graph[x]: #연결된 노드 방문
        if not visited[i]: # 방문하지 않은 노드면 dfs 다시 시작
            dfs(i)
dfs(0)
print(0)