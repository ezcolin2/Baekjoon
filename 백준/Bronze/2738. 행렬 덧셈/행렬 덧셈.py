n, m=map(int, input().split())
matrixA=[]
matrixB=[]
for _ in range(n):
    matrixA.append(list(map(int, input().split())))
for _ in range(n):
    matrixB.append(list(map(int, input().split())))
for r in range(n):
    for c in range(m):
        print(matrixA[r][c]+matrixB[r][c], end=' ')
    print()