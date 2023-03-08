import sys
from bisect import bisect_left
input=sys.stdin.readline
n=int(input())
arr=list(map(int, input().split()))
LIS=[0]
for i in arr:
    if LIS[-1]<i:
        LIS.append(i)
    elif LIS[1]>i:
        LIS[1]=i
    elif LIS[-1]==i:
        continue
    else:
        idx=bisect_left(LIS, i)
        LIS[idx]=i

print(len(LIS)-1)
