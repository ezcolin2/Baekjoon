import sys
input=sys.stdin.readline
parent=[] #각 노드의 부모 노드 
def find_root(x): #x가 속한 트리의 루트 노드 반환 
    if parent[x]==x:
        return x
    return find_root(parent[x])
def union(a, b): #a, b를 하나로 합침
    root_a=find_root(a)
    root_b=find_root(b)
    if root_a<root_b:
        parent[root_b]=a
    else:
        parent[root_a]=b
def kruskal(a, b): #길의 개수
    global parent
    roads=[]
    total_cost=0 #총 비용
    parent=[i for i in range(a)] #각 노드의 부모 노드 
    for _ in range(b):
        roads.append(list(map(int, input().split())))
        total_cost+=roads[-1][2]
    roads.sort(key=lambda x : x[2]) #cost1를 기준으로 오름차순 정렬
    res=0
    for from_node, to_node, cost in roads:
        if find_root(from_node)!=find_root(to_node): #두 노드가 서로 다른 트리에 속해있다면 
            union(from_node, to_node)
            res+=cost
    print(total_cost-res)
while True:
    m, n = map(int, input().split())
    if m==0 and n==0:
        exit()
    kruskal(m, n)