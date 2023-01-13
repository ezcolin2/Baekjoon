import sys
n=int(sys.stdin.readline())
li=list(map(int, sys.stdin.readline().split()))
temp=list(sorted(set(li)))
dic = dict()
for i in range(len(temp)):
    dic[temp[i]]=i
for i in li:
    print(dic[i], end=' ')