import sys
from collections import deque
n=int(sys.stdin.readline())
q=deque([])
for _ in range(n):
    temp=list(sys.stdin.readline().strip('\n').split())
    if len(temp)==2:
        q.append(temp[1])
    elif temp[0]=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif temp[0]=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
    elif temp[0]=='empty':
        print(1 if len(q)==0 else 0)
    elif temp[0]=='size':
        print(len(q))
    elif temp[0]=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
