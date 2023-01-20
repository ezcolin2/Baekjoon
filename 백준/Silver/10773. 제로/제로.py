import sys
n=int(sys.stdin.readline())
stack=[]
for _ in range(n):
    temp=int(sys.stdin.readline())
    if temp==0:
        stack.pop()
    else:
        stack.append(temp)
print(sum(stack))