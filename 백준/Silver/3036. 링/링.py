import sys
def gcd(a, b):
    if(b==0):
        return a
    c = a%b
    return gcd(b, c)
n=int(sys.stdin.readline())
li=list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    temp=gcd(max(li[0], li[i]), min(li[0], li[i]))
    print("{}/{}".format(li[0]//temp, li[i]//temp))