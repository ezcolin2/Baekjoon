import sys
input=sys.stdin.readline
MAX=1e9
def is_cycle(graph, distance, n):
    distance[1]=0 #1번 노드부터 시작
    for i in range(n):
        for from_node, arr in enumerate(graph):
            if from_node==0:
                continue
            for to_node, cost in arr:
                if distance[from_node]+cost<distance[to_node]:
                    distance[to_node]=distance[from_node]+cost
                    if i==n-1:
                        return True
    return False
tc=int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    distance=[MAX]*(n+1) #노드까지의 최단 거리
    graph=[[] for _ in range(n+1)] #그래프
    for _ in range(m):
        s, e, t = map(int, input().split()) #s와 e 사이 이동 시간
        graph[s].append((e, t))
        graph[e].append((s, t))
    for _ in range(w): #웜홀
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))
    if is_cycle(graph, distance, n):
        print('YES')
    else:
        print('NO')