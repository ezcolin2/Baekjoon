import sys
n=int(sys.stdin.readline())
li=[]
for i in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()
for i in li:
    print(i)