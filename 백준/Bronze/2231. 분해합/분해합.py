n=int(input())
li=[0]*(n+1)
for i in range(1, n+1):
    next=i
    for j in str(next):
        next+=int(j)
    if next>n:
        continue
    if li[next]==0:
        li[next]=i
print(li[n])