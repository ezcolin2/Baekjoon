import sys
import heapq
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int ,input().split())
        #그래프 생성
        graph[b].append((a, s))
    
    queue=[] #최소 힙
    cost=[1e9]*(n+1) # 각 컴퓨터의 최소 거리
    cost[0]=0
    heapq.heappush(queue, (0, c)) # (시간, 컴퓨터) 튜플을 넣음
    cost[c]=0 # 처음 감염된 노드는 감염된 상태
    is_min=[False]*(n+1) #확정된 노드
    while queue:
        time, cur = heapq.heappop(queue) #여기서 꺼낸 것은 최단거리 확정
        if time<=cost[cur]:
            for next, t in graph[cur]: #현재 노드에 연결된 링크 조사
                if cost[next]>cost[cur]+t: #거릭 짧다면 갱신
                    cost[next]=cost[cur]+t
                    heapq.heappush(queue, (cost[cur]+t, next))
    cnt=0
    last_cost=0
    for i in cost:
        if i!=1e9:
            cnt+=1
            last_cost=max(last_cost, i)
    print(cnt-1, last_cost)