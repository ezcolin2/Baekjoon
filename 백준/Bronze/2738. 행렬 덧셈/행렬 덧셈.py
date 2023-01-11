import sys
n, m=map(int, sys.stdin.readline().split())
matrixA=[]
matrixB=[]
for _ in range(n):
    matrixA.append(list(map(int, sys.stdin.readline().split())))
for _ in range(n):
    matrixB.append(list(map(int, sys.stdin.readline().split())))
for r in range(n):
    for c in range(m):
        print(matrixA[r][c]+matrixB[r][c], end=' ')
    print()