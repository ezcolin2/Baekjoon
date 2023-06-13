import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
root=[i for i in range(n+1)]
edges=[]
def find_root(x): #노드 x의 부모 찾기
    if root[x]==x: #자신이 부모라는 것은 루트 노드라는 것
        return x
    return find_root(root[x]) #부모의 부모 찾기
def union(a, b): #하나의 트리로 합침
    temp_a=find_root(a)
    temp_b=find_root(b)
    if temp_a>temp_b:
        root[temp_a]=temp_b
    else:
        root[temp_b]=temp_a

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
edges.sort(key=lambda x : x[2]) #가중치를 기준으로 오름차순 정렬
cost=0 #가중치 합 
for a, b, c in edges:
    if find_root(a)!=find_root(b):
        union(a, b)
        cost+=c
print(cost)