import sys
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
mode=[li[0]]
for i in range(1, n):
    if li[i]==li[i-1]:
        le+=1
    if i==n-1 or li[i]!=li[i-1]:
        if res<le:
            res=le
            mode=[li[i-1]]
        elif res==le:
            mode.append(li[i-1])
        le=1
mode.sort()
if len(mode)==1:
    print(mode[0])
else:
    print(mode[1])
print(li[-1]-li[0])