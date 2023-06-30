import sys
input=sys.stdin.readline
a, b = input().rstrip().split()
len_a=len(a)
len_b=len(b)
res=1e9
for i in range(len_b-len_a+1):
    cnt=0
    for j in range(len_a):
        if a[j]!=b[j+i]: # 차이
            cnt+=1
    res=min(res, cnt)
print(res)