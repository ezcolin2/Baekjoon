import sys 
n=int(sys.stdin.readline())
li=[]
for i in range(n):
    li.append(sys.stdin.readline().strip('\n'))
li=list(set(li))
li.sort(key=lambda x : (len(x), x))
for i in li:
    print(i)