import sys
n, m = map(int, sys.stdin.readline().split())
li=[[0 for _ in range(n+1)]]
li+=[[0]+list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        li[i][j]+=li[i-1][j]+li[i][j-1]-li[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(li[x2][y2]-li[x2][y1-1]-li[x1-1][y2]+li[x1-1][y1-1])