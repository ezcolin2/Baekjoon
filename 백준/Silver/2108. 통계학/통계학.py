import sys
from collections import Counter
n=int(input())
li=[]

for i in range(n):
    m=int(sys.stdin.readline())
    li.append(m)

li.sort()
print(round(sum(li)/n))
print(li[n//2])

le=1
res=0

counter = Counter(li)
mode=counter.most_common()
if len(mode)==1 or mode[0][1]!=mode[1][1]:
    print(mode[0][0])
else:
    print(mode[1][0])
print(li[-1]-li[0])