import sys
import string
tmp=string.digits+string.ascii_lowercase
input=sys.stdin.readline
def convert(num, base):
    q, r = divmod(num, base)
    if q==0:
        return tmp[r]
    return convert(q, base)+tmp[r]
def is_palindrome(num):
    if num==num[::-1]:
        return True
    else:
        return False
t=int(input())
for _ in range(t):
    a, n = map(int, input().split())
    if is_palindrome(convert(a, n)):
        print(1)
    else:
        print(0)