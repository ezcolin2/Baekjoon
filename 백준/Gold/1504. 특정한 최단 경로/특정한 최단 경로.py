import sys
import heapq
input=sys.stdin.readline
MAX=1e9
def dijkstra(start, end):
    queue=[]
    time=[MAX]*(n+1)
    time[start]=0
    heapq.heappush(queue, (0, start))
    while queue:
        distance, node = heapq.heappop(queue) # 가장 짧은 간선 가져오기
        if distance <= time[node]: # 작다면
            for next_node, next_distance in graph[node]:
                if time[next_node]>next_distance+time[node]:
                    time[next_node] = next_distance+time[node]
                    heapq.heappush(queue, (next_distance+time[node], next_node))
    return time[end]
n, e = map(int, input().split())
graph=[[] for _ in range(n+1)]  
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
res1 = dijkstra(1, v1)+dijkstra(v1, v2)+dijkstra(v2, n)
res2 = dijkstra(1, v2)+dijkstra(v2, v1)+dijkstra(v1, n)
res = min(res1, res2)
print(res if res<MAX else -1)