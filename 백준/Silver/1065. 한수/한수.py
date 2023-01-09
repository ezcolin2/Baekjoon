cnt=0
def hans(n):
    global cnt
    s=str(n)
    if len(s)==1:
        cnt+=1
        return 0
    se=set()
    for i in range(len(s)-1):
        se.add(int(s[i+1])-int(s[i]))
    if len(se)==1:
        cnt+=1
n=int(input())
for i in range(1,n+1):
    hans(i)
print(cnt)