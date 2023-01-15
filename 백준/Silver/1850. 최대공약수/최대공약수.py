import sys
def gcd(x, y):
    c = x%y
    if c==0:
        return y
    return gcd(y, c)
a, b = map(int, sys.stdin.readline().split())
for _ in range(gcd(max(a, b), min(a, b))):
    print(1, end='')