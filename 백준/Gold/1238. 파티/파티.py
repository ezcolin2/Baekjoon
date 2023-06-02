import sys
import heapq
input=sys.stdin.readline
MAX=1e9
n, m, x = map(int, input().split())
graph=[[] for _ in range(n+1)] #그래프
for _ in range(m): #거리 넣기
    a, b, t = map(int, input().split())
    graph[a].append((b, t)) #a에서 b로 가는데 t시간이 걸림
def dijkstra(start, end): #start에서 end로 가는데 걸리는 최소 시간
    time = [MAX]*(n+1) #start에서 각 노드까지 가는데 걸리는 최소 시간
    time[start] = 0 #시작 노드까지 가는데 걸리는 시간은 0
    queue = [] #최소 힙. 튜플의 첫 번째 값은 걸리는 시간, 두 번째 값은 도착 노드
    heapq.heappush(queue, (0, start)) #튜플의 첫 번째 값인 걸리는 시간은 start 노드부터 걸리는 시간임
    while queue: #큐가 빌 때까지
        t, node = heapq.heappop(queue) #가장 적게 걸리는 노드 가져옴. (확정)
        if node==end:
            return t
        if t<=time[node]: #더 적게 걸린다면
            for node2, time2 in graph[node]: #node와 연결된 인접 노드들 가져옴
                if t+time2<time[node2]: #만약 인접 노드까지의 걸리는 시간이 기존보다 크다면 무시
                    time[node2]=t+time2 #갱신
                    heapq.heappush(queue, (t+time2, node2)) #최단 거리를 결정할 후보 노드들을 넣기
result = 0
for i in range(1, n + 1):
    res = dijkstra(i, x)
    result = max(result, dijkstra(i, x)+dijkstra(x, i))
print(result)