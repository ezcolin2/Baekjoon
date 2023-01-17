import sys
n, m = map(int, sys.stdin.readline().split())
li=[i for i in range(1, n+1)]
res=[]
def perm():
    if len(res)==m:
        for j in res:
            print(j, end=' ')
        print()
    for i in li:
        if i not in res:
            res.append(i)
            perm()
            res.remove(i)
perm()