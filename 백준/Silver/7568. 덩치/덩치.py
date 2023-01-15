import sys 
n=int(sys.stdin.readline())
li=[[] for _ in range(n)]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li[i]=[a, b]
res=[0]*n
for i in range(n):
    cnt=1
    for j in range(n):
        if i==j:
            continue
        if li[i][0]<li[j][0] and li[i][1]<li[j][1]:
            cnt+=1
    res[i]=cnt
for i in res:
    print(i, end=' ')
