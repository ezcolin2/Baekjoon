import sys
n, m = map(int, sys.stdin.readline().split())
li=[i for i in range(1, n+1)]
res=[]
def perm():
    if len(res)==m:
        for i in res:
            print(i, end=' ')
        print()
    else:
        for i in li:
            if len(res)==0 or i>res[-1]:
                res.append(i)
                perm()
                res.remove(i)
perm()