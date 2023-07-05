import sys
input=sys.stdin.readline
v, e = map(int, input().split())
parents=[i for i in range(v+1)]
def find_root(x):
    if parents[x]==x:
        return x
    return find_root(parents[x])
def union(a, b):
    root_a=find_root(a)
    root_b=find_root(b)
    if root_a>root_b:
        parents[root_a]=root_b
    else:
        parents[root_b]=root_a
edges=[list(map(int, input().split())) for _ in range(e)]
edges.sort(key=lambda x : x[2])
res=0
for a, b, cost in edges:
    if find_root(a)==find_root(b):
        continue
    union(a, b)
    res+=cost
print(res)