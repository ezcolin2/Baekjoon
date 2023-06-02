import sys
import heapq
input=sys.stdin.readline
MAX=1e9
n, m, x = map(int, input().split())
graph=[[] for _ in range(n+1)] #그래프
for _ in range(m): #거리 넣기
    a, b, t = map(int, input().split())
    graph[a].append((b, t)) #a에서 b로 가는데 t시간이 걸림
def dijkstra(start):
    time = [MAX]*(n+1)
    time[start]=0
    queue=[]
    heapq.heappush(queue, (0, start))
    while queue:
        t, node = heapq.heappop(queue) #시간이 가장 적게 걸리는 노드
        if t <= time[node]: #시간이 적게 걸린다면 갱신
            for i in graph[node]: #노드에 연결된 인접 노드 조사
                if i[1]+t<time[i[0]]: #시간이 적게 걸린다면 큐에 넣음 (노드를 확정)
                    time[i[0]]=i[1]+t
                    heapq.heappush(queue, (i[1]+t, i[0]))
    return time
result = 0
for i in range(1, n + 1):
    first = dijkstra(i)
    second = dijkstra(x)
    result = max(result, first[x] + second[i])
print(result)