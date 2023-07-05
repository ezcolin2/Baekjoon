import sys
input=sys.stdin.readline
n, r, c = map(int, input().split())
def rec(n, r, c):
    if n==0:
        return 0
    return 2**(2*n-2)*( (r//(2**(n-1)))*2 + c//(2**(n-1))) + rec(n-1, r%(2**(n-1)), c%(2**(n-1)))
print(rec(n, r, c))