import sys
x=[0]*1001
y=[0]*1001
for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    x[a]+=1
    y[b]+=1
print(x.index(1), y.index(1))