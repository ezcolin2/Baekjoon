import sys
li = list(map(int, sys.stdin.readline().split()))
while li.count(0)!=3:
    m=max(li)
    li.remove(m)
    if li[0]**2+li[1]**2==m**2:
        print("right")
    else:
        print("wrong")
    li = list(map(int, sys.stdin.readline().split()))
