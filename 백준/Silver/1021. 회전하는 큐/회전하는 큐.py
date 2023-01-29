import sys
from collections import deque
input=sys.stdin.readline
n,m = map(int, input().split())
dq=deque([i+1 for i in range(n)])
order=list(map(int, input().split()))
cnt=0
for i in order:
    idx=dq.index(i)
    if idx<=len(dq)//2:
        dq.rotate(-idx)
        dq.popleft()
        cnt+=idx
    
    else:
        dq.rotate(len(dq)-idx)
        cnt+=len(dq)-idx
        dq.popleft()
print(cnt)