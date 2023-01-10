import sys
n=int(input())
stack=[]
for _ in range(n):
    temp=sys.stdin.readline().split()
    if len(temp)==2:
        stack.append(temp[1])
    elif temp[0]=="pop":
        if len(stack)==0:
            print(-1)
            continue
        print(stack.pop())
    elif temp[0]=="size":
        print(len(stack))
    elif temp[0]=="empty":
        print("1" if len(stack)==0 else "0")
    else:
        if len(stack)==0:
            print(-1)
            continue
        print(stack[-1])