import sys
matrix = [[] for _ in range(9)]
for i in range(9):
    matrix[i] = list(map(int, sys.stdin.readline().split()))
row_max=[0 for _ in range(9)]
m=0
for i in range(9):
    m=max(m, max(matrix[i]))
for i in range(9):
    if m not in matrix[i]:
        continue
    print(m)
    print(i+1, matrix[i].index(m)+1)
    exit()