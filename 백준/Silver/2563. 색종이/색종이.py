import sys
matrix=[[1 for _ in range(101)] for _ in range(101)]
n=int(input())
for _ in range(n):
    a, b = map(int , sys.stdin.readline().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            matrix[i][j]=0
res=0
for i in range(101):
    res+=matrix[i].count(0)
print(res)