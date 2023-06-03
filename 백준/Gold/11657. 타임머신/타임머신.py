import sys
input=sys.stdin.readline
MAX=1e9
n, m = map(int, input().split())
graph=[[] for _ in range(n+1)] #그래프
arr=[MAX]*(n+1)
arr[1]=0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) #a에서 b로 가는 시간은 c
for i in range(n): 
    for idx, temp in enumerate(graph): #모든 간선 조사
        if idx==0:
            continue
        for to_node, cost in temp:
            if arr[idx]!=MAX and arr[idx]+cost<arr[to_node]: #현재 까지 to_node까지의 비용보다 지금 노드를 거쳐 가는 편이 저렴할 때
                arr[to_node]=arr[idx]+cost #최단 거리 갱신
                if i==n-1: #사이클이 존재
                    print(-1)
                    exit()
for i in range(2, n+1):
    if arr[i]==MAX:
        print(-1)
    else:
        print(arr[i])