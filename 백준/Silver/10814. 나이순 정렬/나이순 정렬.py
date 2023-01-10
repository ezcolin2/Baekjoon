import sys
n=int(input())
li=[]
for i in range(n):
    a, b = sys.stdin.readline().split()
    a=int(a)
    li.append([a,b])
li.sort(key=lambda x:x[0])
for i in li:
    print(i[0], i[1])
