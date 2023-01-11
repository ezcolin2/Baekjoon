import sys
total=int(input())
n=int(input())
res=0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    res+=a*b
print("Yes" if res==total else "No")
