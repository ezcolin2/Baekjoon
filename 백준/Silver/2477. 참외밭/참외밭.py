import sys
n=int(sys.stdin.readline())
dis=[0]*5
li=[]
for _ in range(6):
    a, b = map(int, sys.stdin.readline().split())
    dis[a]+=1
    li.append([a, b])
two=set([])
for i in range(len(dis)):
    if dis[i]==2:
        two.add(i)
res=[]
interrupt=False
temp=[]
for i in li:
    if i[0] in two:
        if interrupt:
            temp.append(i)
        else:
            res.append(i)
    elif len(res)!=4:
        interrupt=True

res=temp+res
blank=res[1][1]*res[2][1]
whole=1
for i in li:
    if i[0] not in two:
        whole*=i[1]
print(n*(whole-blank))