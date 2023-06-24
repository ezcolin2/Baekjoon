import sys
INF=1e9
input=sys.stdin.readline
start=tuple(map(float, input().split()))
end=tuple(map(float, input().split()))
n=int(input())
canons=[start]
for _ in range(n):
    canons.append(tuple(map(float, input().split())))
canons.append(end)
v=len(canons)
#모든 쌍의 점에 대해서 거리 구하기
graph=[[INF]*v for _ in range(v)]
for i in range(v):
    for j in range(v):
        if i==j:
            graph[i][j]=0
        else:
            s_canon=canons[i] #시작 대포 
            e_canon=canons[j] #도착 대포
            distance=((s_canon[0]-e_canon[0])**2+(s_canon[1]-e_canon[1])**2)**0.5 #거리 구하기
            if i==0 or i==v-1: #a에서는 걸어갈 수 밖에 없음
                graph[i][j]=distance/5
            else:
                graph[i][j]=min(distance/5, abs(distance-50)/5+2)
# 다익스트라 시작
visited=[False]*v #최단 거리 확정 여부
res=[INF]*v
#시작 점은 확정됨
visited[0]=True
res[0]=0
current=0
while(True):
    if visited[v-1]:
        break
    #일단 연결된 노드들 최단거리 갱신
    for i in range(v):
        res[i]=min(res[i], res[current]+graph[current][i])
    #가장 짧은 거리 찾기
    current_distance=INF 
    for i in range(v):
        #아직 거리가 확정나지 않은 노드들 중 가장 짧은 노드
        if res[i]<current_distance and not visited[i]:
            current=i
            current_distance=res[i]
    visited[current]=True
print(res[v-1])