import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
d=deque()
res=[]
for i in range(1, n+1):
    d.append(i)
while len(d)!=0:
    for _ in range(k-1):
        d.append(d.popleft())
    res.append(d.popleft())
print('<', end='')
for i in range(len(res)):
    if i==len(res)-1:
        print(res[i],end='>')
    else:
        print(res[i], end=', ')