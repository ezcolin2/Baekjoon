import sys
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    dic = dict()
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        if b not in dic:
            dic[b]=1
        else:
            dic[b]+=1
    res=1
    for i in dic.keys():
        res*=(dic[i]+1)
    print(res-1)