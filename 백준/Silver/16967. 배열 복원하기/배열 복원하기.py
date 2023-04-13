import sys
input=sys.stdin.readline
h, w, x, y = map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(h+x)]
res=[[0]*w for _ in range(h)]
for i in range(x):#안 겹치는 부분 추가
    for j in range(w):
        res[i][j]=arr[i][j]
for i in range(h):
    for j in range(y):
        res[i][j]=arr[i][j]
for i in range(x, h):
    for j in range(y, w):
        res[i][j]=arr[i][j]-res[i-x][j-y]
for i in range(h):
    for j in range(w):
        print(res[i][j], end=' ')
    print()