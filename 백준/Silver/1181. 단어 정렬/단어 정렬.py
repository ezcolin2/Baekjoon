n=int(input())
li=[]
for i in range(n):
    li.append(input())
li=list(set(li))
li.sort(key=lambda x : (len(x), x))
for i in li:
    print(i)