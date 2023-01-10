import sys
n=int(input())
num=[0]*10001
for _ in range(n):
    num[int(sys.stdin.readline())]+=1
for i in range(1, 10001):
    while num[i]>0:
        print(i)
        num[i]-=1