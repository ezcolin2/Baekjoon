import sys 
n=int(sys.stdin.readline())
for _ in range(n):
    ps=sys.stdin.readline().strip('\n')
    stack=0
    con=False
    for i in ps:
        if i=='(':
            stack+=1
        else:
            stack-=1
        if stack<0:
            print("NO")
            con=True
            break
    if con:
        continue
    if stack==0:
        print("YES")
    else:
        print("NO")