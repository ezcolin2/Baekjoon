import sys 
n=int(sys.stdin.readline())
for _ in range(n):
    ps=sys.stdin.readline().strip('\n')
    left=0
    right=0
    con=False
    for i in ps:
        if i=='(':
            left+=1
        else:
            right+=1
        if right>left:
            print("NO")
            con=True
            break
    if con:
        continue
    if left==right:
        print("YES")
    else:
        print("NO")