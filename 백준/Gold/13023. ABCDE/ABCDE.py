import sys
input=sys.stdin.readline
def DFS(k, cnt):
    if cnt==5:
        print(1)
        exit()
    for i in arr[k]: #연결된 거 조사
        if not visited[i]: #아직 방문안했으면 방문
            visited[i]=True
            DFS(i, cnt+1)
            visited[i]=False

visited=[False]*2000
n, m = map(int, input().split())
arr=[[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(n):
    visited[i]=True
    DFS(i, 1)
    visited[i]=False
print(0)