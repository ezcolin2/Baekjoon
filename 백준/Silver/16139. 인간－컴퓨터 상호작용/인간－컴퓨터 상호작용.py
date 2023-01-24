import sys
s=sys.stdin.readline().strip('\n')
n=int(sys.stdin.readline())
li=[[0]*len(s) for _ in range(26)]
for idx, val in enumerate(s):
    li[ord(val)-ord('a')][idx]+=1
for i in range(26):
    for j in range(1, len(s)):
        li[i][j]+=li[i][j-1]
for _ in range(n):
    a, l, r= sys.stdin.readline().strip('\n').split()
    l = int(l)
    r=int(r)
    if l==0:
        print(li[ord(a)-ord('a')][r])
    else:
        print(li[ord(a)-ord('a')][r]-li[ord(a)-ord('a')][l-1])
    