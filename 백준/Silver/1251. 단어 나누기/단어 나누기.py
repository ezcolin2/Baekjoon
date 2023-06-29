import sys
input=sys.stdin.readline
s=input().rstrip()
res=[]
for i in range(len(s)-2):
    for j in range(i+1, len(s)-1):
        res.append("".join(reversed(s[:i+1]))+"".join(reversed(s[i+1:j+1]))+"".join(reversed(s[j+1:])))
print(min(res))
