import sys
n=int(input())
li=[]
for i in range(n):
    temp = sys.stdin.readline().split()
    temp[1:]=list(map(int, temp[1:]))
    li.append(temp)
li.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in li:
    print(i[0])